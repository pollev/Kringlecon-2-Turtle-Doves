# Kringlecon 2: Turtle Doves
This writeup is the collaborative work of:
- Polle Vanhoof
- Jan D'Herdt
- Honorable Mention goes out to Tudor Azoitei

For the 2019 SANS holiday hack challenge, Jan and myself decided to work together and tackle the interesting challenges presented by the SANS team. In the end, we completed all the challenges and objectives. As a nice bonus, we even stubled upon an oversight that allowed us to bypass all challenges and complete the game without completing any challenge.

We hope you enjoy this writeup as much as we enjoyed the game.

-----------------------------
## Table of Contents

This writeup is split into several sections

1. [Information Gathering](#information-gathering)
   1. [Interacting with the game over websocket](#interacting-with-the-game-over-websocket)
   2. [Locations and Notable Characters](#locations-and-notable-characters)
   3. [Oversight: End-Credits Bypass](#oversight-end-credits-bypass)
2. [Terminal Challenges](#terminal-challenges)
   1. [Escape Ed](#escape-ed)
   2. [Frosty Keypad](#frosty-keypad)
   3. [Linux Path](#linux-path)
   4. [Nyanshell](#nyanshell)
   5. [Mongo Pilfer](#mongo-pilfer)
   6. [Smart Braces](#smart-braces)
   7. [Holiday Hack Trail](#holiday-hack-trail)
   8. [Graylog](#graylog)
   9. [Powershell Laser](#powershell-laser)
   10. [Sleigh Route Finder](#sleigh-route-finder)
3. [Objectives](#objectives)
   0. [Talk to Santa in the Quad](#talk-to-santa-in-the-quad)
   1. [Find the Turtle Doves](#find-the-turtle-doves)
   2. [Unredact Threatening Document](#unredact-threatening-document)
   3. [Windows Log Analysis: Evaluate Attack Outcome](#windows-log-analysis-evaluate-attack-outcome)
   4. [Windows Log Analysis: Determine Attacker Technique](#windows-log-analysis-determine-attacker-technique)
   5. [Network Log Analysis: Determine Compromised System](#network-log-analysis-determine-compromised-system)
   6. [Splunk](#splunk)
   7. [Get Access To The Steam Tunnels](#get-access-to-the-steam-tunnels)
   8. [Bypassing the Frido Sleigh CAPTEHA](#bypassing-the-frido-sleigh-capteha)
   9. [Retrieve Scraps of Paper from Server](#retrieve-scraps-of-paper-from-server)
   10. [Recover Cleartext Document](#recover-cleartext-document)
   11. [Open the Sleigh Shop Door](#open-the-sleigh-shop-door)
   12. [Filter Out Poisoned Sources of Weather Data](#filter-out-poisoned-sources-of-weather-data)
4. [Addendum](#addendum)

-----------------------------
## Information Gathering
### Interacting with the game over websocket

The game started on a Friday evening and my colleague and I had agreed to start it together on Monday.
As a result, I was eagerly looking at the start of the event and trying to do anything other than actually working on the challenges.

I figured I would see how the game worked behind the scenes and started looking at the websocket traffic between my client and the server.
This quickly turned into a small project of itself. Soon I had a small script running and I decided I would use it to handle most of the information gathering.
A few hours later and [santas_little_helper.py](https://github.com/pollev/santas_little_helper) was born.

The following sections group the data we collected through the script.

-----------------------------
### Locations and Notable Characters
#### Zone: The Quad
Map:
```
           111            111
           111            111
           111            111
           111            111
           111            111
           111            111
   1111111111111111111111111111111111111
   1111111111111111111111111111111111111
   1111111111111111111111111111111111111
 111111111111111111111111111111111111111
 111111111111111111111111111111111111111
 111111111111111111111111111111111111111
 111111111111111111111111111111111111111
 111111111111111111111111111111111111111
 111111111111111111111111111111111111111
 111111111111111111111111111111111111111
 111111111111111111111111111111111111111
 111111111111111111111111111111111111111
 111111111111111111111111111111111111111
 111111111111111111111111111111111111111
 111111111111111111111111111111111111111
 111111111111111111111111111111111111111
 111111111111111111111111111111111111111
 111111111111111111111111111111111111111
 11111111111111111     11111111111111111
111111111111111111     111111111111111111
111111111111111111     111111111111111111
 11111111111111111     111111111111111
 11111111111111111     111111111111111
 1111111111111111111111111111111111111
 1111111111111111111111111111111111111
 111111111111111111111111111111111111111
 111111111111111111111111111111111111111
 111111111111111111111111111111111111111
 111111111111111111111111111111111111111
 111111111111111111111111111111111111111
 111111111111111111111111111111111111111
 111111111111111111111111111111111111111
 111111111111111111111111111111111111111
 1111111111111111111 1111111111111111111
 1111111111111111111 1111111111111111111
 111111111111111111111111111111111111111
 111111111111111111111111111111111111111
 111111111111111111111111111111111111111
 111111111111111111111111111111111111111
 111111111111111111111111111111111111111
                   111
```

NPCs:
- Santa
- Tangle Coalbox

Terminals:
- Frosty Keypad

#### Zone: Student Union
Map:
```
1   11   1    11   1   1
11 1111 11    111 111 11
1111111111 1111111111111
111111111111111111111111 1
111111111111111111111111 1
11111111111111111111111111
111111111111  111111111111
  1111111111  1111111111111
  1111111111111111111111111
111111111111111111111111111
111111111111111111111111111
   111            111
```

NPCs:
- Shinny Upatree
- Kent Tinseltooth
- Google Booth
- SANS.edu Booth
- Splunk Booth
- Swag Booth
- Michael and Jane - Two Turtle Doves

Terminals:
- Smart Braces

#### Zone: Sleigh Workshop
Map:
```
           1
   111  111111
    11  1111
111 11  1111
11111111111111
11111111111111
1111111111 111
1111111111 111
1111  1  11111
11111111111111
 1
```

NPCs:
- Wunorse Openslae
- Krampus
- The Tooth Fairy

Terminals:
- Zeek JSON Analysis
- Sleigh Route Finder

#### Zone: The Bell Tower
Map:
```
111111
111
111 1 1
1 111 1
1 11111
1111111
1111111
      1
```

NPCs:
- Krampus
- The Tooth Fairy
- Santa
- Tooth

Terminals:

#### Zone: Hermey Hall
Map:
```
      1     1
    1111  111111
    1111  111111
  11111111111111  1   1   1   1   1   1   1
1111111111111111 111111111111111111111111111
11111111111111111111111111111111111111111111
11111111111111111111111111111111111111111111
11111111111111111111111111111111111111111111
  11111111111111
  11111111111111
        111
```

NPCs:
- SugarPlum Mary

Terminals:
- Linux Path

#### Zone: NetWars
Map:
```
111111111111111
111111111111  1
11    111     1
111111111111111
111111111111111
111111111111111
11    111    11
111111111111111
111111111111111
111111111111111
       1
```

NPCs:
- Holly Evergreen

Terminals:
- Mongo Pilfer

#### Zone: Speaker UNpreparedness Room
Map:
```
   11111
   11111
11111  1
11111  1
11111111
11111111
11111111
  1
```

NPCs:
- Alabaster Snowball

Terminals:
- Nyanshell

#### Zone: Track 1 to Track 7
Map:
```
1111111
1111111
1111111
1111111
1111111
1111111
1111111
1111111
1111111
   1
```

NPCs:

Terminals:

#### Zone: The Laboratory
Map:
```
111111111
1111111111 111
1111111111 111
111    1111111
11     11111111
11  11111111111
111111111111111
111111111111111
11111111111111
```

NPCs:
- Sparkle Redberry
- Professor Banas

Terminals:
- Xmas Cheer Laser

#### Zone: Dorm
Map:
```
         11111111111111
           1111  111111
           1111  111111            1
1111111111111111111111111111  1111111
1111111111111111111111111111  1111111
111111111111 111111 11111111111111111
1111111111111111111111111111111111111
         11111111111111
         11111111111111
               111
```

NPCs:
- Pepper Minstix
- Minty Candycane

Terminals:
- Holiday Hack Trail
- Graylog

#### Zone: Minty's Dorm Room
Map:
```
      1
  1   1
  111111
  111111
11111111
11111111
  1
```

NPCs:

Terminals:
- Key Cutting Machine

#### Zone: Minty's Closet
Map:
```
 1
 11
111
111
 1
```

NPCs:

Terminals:
- Mysterious Locked Door

#### Zone: Steam Tunnels
Map:
```
 11111
11111111111111
111111111111111
111111111111111
 11111      111
   1        111
            111
            111
            111
            111
            111
            111
            111
            111       1111111   1
            111      111111111 11
            1111111111111111 1111
            1111111111111111 1111
            111111111111111111111
                     111111111111
```

NPCs:
- Krampus

Terminals:
- Frido Sleigh Contest

#### Zone: Train Station
Map:
```
         11111
         11111
         11111
         11111
11111111111111111111111
111111111111111111111
  1111111111 1111  11
  1111111111 1111  1111
11111111111111111111111
11111111111111111111111
11111111111111111111111
11111111111111111111111
```

NPCs:
- Bushy Evergreen
- Santa

Terminals:
- Escape Ed


-----------------------------
### Oversight: End-Credits Bypass
While working on the data gathering script, I realized that I would need to automate the movement from room to room. The script could only pull data for a location after physically moving my character there. So I started working on a 'teleportation' option. The script interacts with the backend directly to move my character to each room, it then grabs all zone information it finds and stores it.

That info includes the new exit-portals for that specific zone. That means that, once we enter a zone, we can automatically figure out new locations we can go to and the script can then automate going to those new zones as well.

It turns out however that certain zones, which are supposed to only be accessible after completion of an objective, are still accessible if interacting with the websocket in this manner.
It is the client which refuses to enter these zones. The portals to the zones still exist, and we can force our way in by sending the appropriate command to the server. It seems the devs forgot to do some server side validation here.

After discovering this, I added a 'teleportation' feature to the script. Which can teleport your character directly to any zone (including the finale zone)
```
polle@polle-pc$ ./santas_little_helper.py -t

.▄▄ ·  ▄▄▄·  ▐ ▄ ▄▄▄▄▄ ▄▄▄· .▄▄ ·     ▄▄▌  ▪  ▄▄▄▄▄▄▄▄▄▄▄▄▌  ▄▄▄ .     ▄ .▄▄▄▄ .▄▄▌   ▄▄▄·▄▄▄ .▄▄▄         {_}
▐█ ▀. ▐█ ▀█ •█▌▐█•██  ▐█ ▀█ ▐█ ▀.     ██•  ██ •██  •██  ██•  ▀▄.▀·    ██▪▐█▀▄.▀·██•  ▐█ ▄█▀▄.▀·▀▄ █·      *-=\
▄▀▀▀█▄▄█▀▀█ ▐█▐▐▌ ▐█.▪▄█▀▀█ ▄▀▀▀█▄    ██▪  ▐█· ▐█.▪ ▐█.▪██▪  ▐▀▀▪▄    ██▀▐█▐▀▀▪▄██▪   ██▀·▐▀▀▪▄▐▀▀▄          \____(
▐█▄▪▐█▐█ ▪▐▌██▐█▌ ▐█▌·▐█ ▪▐▌▐█▄▪▐█    ▐█▌▐▌▐█▌ ▐█▌· ▐█▌·▐█▌▐▌▐█▄▄▌    ██▌▐▀▐█▄▄▌▐█▌▐▌▐█▪·•▐█▄▄▌▐█•█▌        _|/---\
 ▀▀▀▀  ▀  ▀ ▀▀ █▪ ▀▀▀  ▀  ▀  ▀▀▀▀     .▀▀▀ ▀▀▀ ▀▀▀  ▀▀▀ .▀▀▀  ▀▀▀     ▀▀▀ · ▀▀▀ .▀▀▀ .▀    ▀▀▀ .▀  ▀        \        \
 - A Kringlecon 2019 tool by Polle Vanhoof

[+] Loading portal data from portal_data.json
[+] Loading extra info from extra_info.json
[*] Starting login for user d8489526@urhen.com
[-] WARNING: Plaintext credentials in script
[*] Server new current location: trainstation

[+] Starting teleportation module. Where would you like to go?
[>] Your current zone is trainstation
- quad (The Quad)
- studentunion (Student Union)
- sleighshop (Sleigh Workshop)
- finale (The Bell Tower)
- hermeyhall (Hermey Hall)
- netwars (NetWars)
- speakerroom (Speaker UNpreparedness Room)
- track1 (Track 1)
- track2 (Track 2)
- track3 (Track 3)
- track4 (Track 4)
- track5 (Track 5)
- track6 (Track 6)
- track7 (Track 7)
- library (The Laboratory)
- dorm (Dorm)
- mintydorm (Minty's Dorm Room)
- mintycloset (Minty's Closet)
- steamtunnels (Steam Tunnels)
- trainstation (Train Station)

Please enter the zone shortname you would like to teleport to: finale
[!] Full multi-zone move from trainstation to finale
[!] Moving from room trainstation to quad_north
[*] Server new current location: quad
[!] Moving from room quad to unionleft
[*] Server new current location: studentunion
[!] Moving from room studentunion to sleighshop
[*] Server new current location: sleighshop
[!] Moving from room sleighshop to finale
[*] Server new current location: finale

[+] DONE!
```
This allows you to access the credits without ever completing a single challenge.
![easy victory 1](images/victory_bypass.png)
![easy victory 2](images/victory_bypass_2.png)

... And that is the story of how I had to tell my colleague why I had already completed the game even though we had agreed not to play. These things happen...

-----------------------------
## Terminal Challenges

Alright, with that out of the way, let us move on to the actual challenges!

### Escape Ed
#### Context
Initial Dialog:
Bushy Evergreen
> Hi, I'm Bushy Evergreen.  Welcome to Elf U!
> I'm glad you're here. I'm the target of a terrible trick.
> Pepper Minstix is at it again, sticking me in a text editor.
> Pepper is forcing me to learn ed.
> Even the hint is ugly. Why can't I just use Gedit?
> Please help me just quit the grinchy thing.


Completed Dialog:
Bushy Evergreen
> Wow, that was much easier than I'd thought.
> Maybe I don't need a clunky GUI after all!
> Have you taken a look at the password spray attack artifacts?
> I'll bet that DeepBlueCLI tool is helpful.
> You can check it out on GitHub.
> It was written by that Eric Conrad.
> He lives in Maine - not too far from here!


Challenge-url:  
https://docker2019.kringlecon.com/?challenge=edescape


Location:  
trainstation (Train Station)


#### Solution
Ed is a really old text editor, we can exit it with a simple command:
```
Type 'Q' and enter
```

-----------------------------
### Frosty Keypad
#### Context
Initial Dialog:
Tangle Coalbox
> Hey kid, it's me, Tangle Coalbox.
> I'm sleuthing again, and I could use your help.
> Ya see, this here number lock's been popped by someone.
> I think I know who, but it'd sure be great if you could open this up for me.
> I've got a few clues for you.
>  1. One digit is repeated once.
>  2. The code is a prime number.
>  3. You can probably tell by looking at the keypad which buttons are used.


Completed Dialog:
Tangle Coalbox
> Yep, that's it. Thanks for the assist, gumshoe.
> Hey, if you think you can help with another problem, Prof. Banas could use a hand too.
> Head west to the other side of the quad into Hermey Hall and find him in the Laboratory.


Challenge-url:  
https://keypad.elfu.org?challenge=keypad


Location:  
quad (The Quad)


#### Solution
We have a look at the door keypad and see that the keys "1", "3" and "7" have been used.
We are also told that one of those numbers is used twice.

The immediate thing to try would be "1337" (or 'leet'). However this number is not prime. We could solve this challenge by grabbing a list of primes from the internet and removing all entries that have a digit not equal to 1, 3 or 7. We could then remove all entries that do not have a duplicate digit. We can then just write a script to try all the remaining possibilities.

Or, what we did is just to try the first options that came to our mind, and we tried '7331' (the reverse of 1337) and got lucky.
![keypad](images/keypad_code.png)

That's all there is to this challenge, we do however find a little easter egg on the wall inside the dorm after we enter the now unlocked door. It seems the ElfU students need a reminder sometimes and have written the code down on the wall.
![keypad_egg](images/keypad_egg.png)

-----------------------------
### Linux Path
todo

-----------------------------
### Nyanshell
todo

-----------------------------
### Mongo Pilfer
todo

-----------------------------
### Smart Braces
todo

-----------------------------
### Holiday Hack Trail
todo

-----------------------------
### Graylog
todo

-----------------------------
### Powershell Laser
todo

-----------------------------
### Sleigh Route Finder
todo


-----------------------------
## Objectives
todo


## Addendum
todo
