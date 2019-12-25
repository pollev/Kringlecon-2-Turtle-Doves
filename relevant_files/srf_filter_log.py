#!/usr/bin/env python3

import glob
import os
import math

# Bash colors
off='\033[0m'       # Text Reset
red='\033[0;91m'          # Red
grn='\033[0;32m'        # Green
yel='\033[0;33m'       # Yellow

input_file = 'http.log'
malicious_requests = 'malicious_requests.log'
malicious_agents = 'malicious_agents.log'
filter_list = {}

filter_commands = [
        '''jq '. | select (.username | contains("'"'"'")) | ."id.orig_h"' > filters/sql_injection_username.filter''',
        '''jq '. | select (.uri | contains("'"'"'")) | ."id.orig_h"' > filters/sql_injection_uri.filter''',
        '''jq '. | select (.user_agent | contains("'"'"'")) | ."id.orig_h"' > filters/sql_injection_agent.filter''',
        '''jq '. | select (.uri | contains("<")) | ."id.orig_h"' > filters/xss_uri.filter''',
        '''jq '. | select (.host | contains("<")) | ."id.orig_h"'> filters/xss_host.filter''',
        '''jq '. | select (."uri" | contains("pass")) | ."id.orig_h"' > filters/lfi_pass.filter''',
        '''jq '. | select (."user_agent" | contains(":; };")) | ."id.orig_h"' > filters/shell_shock.filter''',
        ]


def create_filters():
    good(f"Removing all filter files")
    os.system('rm filters/*.filter')
    good(f"Creating filter files")
    for command in filter_commands:
        cmd = f"cat {input_file} | {command}"
        info(f"Executing: {cmd}")
        os.system(cmd)


def load_filters():
    global filter_list
    good(f"Loading list of bad ip addresses. Using all files with {yel}'.filter'{grn} extension")
    for filename in glob.glob('filters/*.filter'):
        info(f"Loading filter {filename}")
        ip_list = list()
        with open(filename) as f:
            content = f.readlines()
        for line in content:
            ip = line.replace('"', '')
            ip = ip.replace("\n", '')
            ip_list.append(ip)
        filter_list[filename] = ip_list


def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def filter_ips():
    good(f"Selecting all bad ips from file {yel}{input_file}{grn} and writing to output {yel}{malicious_requests}{grn}")
    all_bad_ips = list()
    for filt in filter_list:
        all_bad_ips.extend(filter_list[filt])
    info("Removing all duplicate ips")
    all_bad_ips = list(dict.fromkeys(all_bad_ips))
    info(f"number of bad ips: {len(all_bad_ips)}")

    infile = input_file
    outfile = malicious_requests
    chunk_size = 100
    iteration = 0
    os.system(f"echo '' > {outfile}")
    for chunk in chunks(all_bad_ips, chunk_size):
        iteration = iteration + 1
        print(f"Filtering ip block {iteration} / {math.ceil(len(all_bad_ips) / chunk_size)}")
        filter_ips_partial(chunk, infile, outfile)

    good("Completed filtering of original file")


def filter_ips_partial(ips, infile, outfile):
    jq_command = f"cat {infile} | jq ' . | select(.\"id.orig_h\" | "
    for ip in ips:
        jq_command = jq_command + f"contains(\"{ip}\") or "
    jq_command = jq_command[:-4]
    jq_command = jq_command + f")' >> {outfile}"
    info(f"Executing: {jq_command}")
    os.system(jq_command)


def output_bad_user_agents():
    good(f"Creating list of all user agents used by malicious requests (file {malicious_requests}) and writing to file {malicious_agents}")
    command = f"cat {malicious_requests}" + ''' | jq '. | .user_agent' | sort -u''' + f" > {malicious_agents}"
    info(f"Executing: {command}")
    os.system(command)

def main():
    info("Starting filtering script.")
    create_filters()
    load_filters()
    filter_ips()
    output_bad_user_agents()


def err(msg):
    print(f"{red}[-] {msg}{off}")

def good(msg):
    print(f"{grn}[+] {msg}{off}")

def info(msg):
    print(f"[*] {msg}")

main()
