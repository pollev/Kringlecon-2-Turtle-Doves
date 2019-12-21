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


#### MOTD
When we start the terminal, we are greeted with the following message:
```
                  ........................................
               .;oooooooooooool;,,,,,,,,:loooooooooooooll:
             .:oooooooooooooc;,,,,,,,,:ooooooooooooollooo:
           .';;;;;;;;;;;;;;,''''''''';;;;;;;;;;;;;,;ooooo:
         .''''''''''''''''''''''''''''''''''''''''';ooooo:
       ;oooooooooooool;''''''',:loooooooooooolc;',,;ooooo:
    .:oooooooooooooc;',,,,,,,:ooooooooooooolccoc,,,;ooooo:
  .cooooooooooooo:,''''''',:ooooooooooooolcloooc,,,;ooooo,
  coooooooooooooo,,,,,,,,,;ooooooooooooooloooooc,,,;ooo,
  coooooooooooooo,,,,,,,,,;ooooooooooooooloooooc,,,;l'
  coooooooooooooo,,,,,,,,,;ooooooooooooooloooooc,,..
  coooooooooooooo,,,,,,,,,;ooooooooooooooloooooc.
  coooooooooooooo,,,,,,,,,;ooooooooooooooloooo:.
  coooooooooooooo,,,,,,,,,;ooooooooooooooloo;
  :llllllllllllll,'''''''';llllllllllllllc,



Oh, many UNIX tools grow old, but this one's showing gray.
That Pepper LOLs and rolls her eyes, sends mocking looks my way.
I need to exit, run - get out! - and celebrate the yule.
Your challenge is to help this elf escape this blasted tool.

-Bushy Evergreen

Exit ed.

1100
```

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

Or you could do what we did, try the first options that come to your mind, one of them being '7331' (the reverse of 1337) and get lucky.
![keypad](images/keypad_code.png)

That's all there is to this challenge, we do however find a little easter egg on the wall inside the dorm after we enter the now unlocked door. It seems the ElfU students need a reminder sometimes and have written the code down on the wall.
![keypad_egg](images/keypad_egg.png)

-----------------------------
### Linux Path
#### Context
Initial Dialog:
SugarPlum Mary
> Oh me oh my - I need some help!
> I need to review some files in my Linux terminal, but I can't get a file listing.
> I know the command is *ls*, but it's really acting up.
> Do you think you could help me out? As you work on this, think about these questions:
> 1. Do the words in green have special significance?
> 2. How can I find a file with a specific name?
> 3. What happens if there are multiple executables with the same name in my $PATH?


Completed Dialog:
SugarPlum Mary
> Oh there they are!  Now I can delete them.  Thanks!
> Have you tried the Sysmon and EQL challenge?
> If you aren't familiar with Sysmon, Carlos Perez has some great info about it.
> Haven't heard of the Event Query Language?
> Check out some of [Ross Wolf](https://www.endgame.com/our-experts/ross-wolf)'s work on EQL or that blog post by Josh Wright in your badge.


Challenge-url:  
https://docker2019.kringlecon.com/?challenge=path


Location:  
Hermey Hall

#### MOTD
When we start the terminal, we are greeted with the following message:
```
K000K000K000KK0KKKKKXKKKXKKKXKXXXXXNXXXX0kOKKKK0KXKKKKKKK0KKK0KK0KK0KK0KK0KK0KKKKKK
00K000KK0KKKKKKKKKXKKKXKKXXXXXXXXNXXNNXXooNOXKKXKKXKKKXKKKKKKKKKK0KKKKK0KK0KK0KKKKK
KKKKKKKKKKKXKKXXKXXXXXXXXXXXXXNXNNNNNNK0x:xoxOXXXKKXXKXXKKXKKKKKKKKKKKKKKKKKKKKKKKK
K000KK00KKKKKKKKXXKKXXXXNXXXNXXNNXNNNNNWk.ddkkXXXXXKKXKKXKKXKKXKKXKKXK0KK0KK0KKKKKK
00KKKKKKKKKXKKXXKXXXXXNXXXNXXNNNNNNNNWXXk,ldkOKKKXXXXKXKKXKKXKKXKKKKKKKKKK0KK0KK0XK
KKKXKKKXXKXXXXXNXXXNXXNNXNNNNNNNNNXkddk0No,;;:oKNK0OkOKXXKXKKXKKKKKKKKKKKKK0KK0KKKX
0KK0KKKKKXKKKXXKXNXXXNXXNNXNNNNXxl;o0NNNo,,,;;;;KWWWN0dlk0XXKKXKKXKKXKKKKKKKKKKKKKK
KKKKKKKKXKXXXKXXXXXNXXNNXNNNN0o;;lKNNXXl,,,,,,,,cNNNNNNKc;oOXKKXKKXKKXKKXKKKKKKKKKK
XKKKXKXXXXXXNXXNNXNNNNNNNNN0l;,cONNXNXc',,,,,,,,,KXXXXXNNl,;oKXKKXKKKKKK0KKKKK0KKKX
KKKKKKXKKXXKKXNXXNNXNNNNNXl;,:OKXXXNXc''',,''''',KKKKKKXXK,,;:OXKKXKKXKKX0KK0KK0KKK
KKKKKKKKXKXXXXXNNXXNNNNW0:;,dXXXXXNK:'''''''''''cKKKKKKKXX;,,,;0XKKXKKXKKXKKK0KK0KK
XXKXXXXXXXXXXNNNNNNNNNN0;;;ONXXXXNO,''''''''''''x0KKKKKKXK,',,,cXXKKKKKKKKXKKK0KKKX
KKKKKKKXKKXXXXNNNNWNNNN:;:KNNXXXXO,'.'..'.''..':O00KKKKKXd'',,,,KKXKKXKKKKKKKKKKKKK
KKKKKXKKXXXXXXXXNNXNNNx;cXNXXXXKk,'''.''.''''.,xO00KKKKKO,'',,,,KK0XKKXKKK0KKKKKKKK
XXXXXXXXXKXXXXXXXNNNNNo;0NXXXKKO,'''''''.'.'.;dkOO0KKKK0;.'',,,,XXXKKK0KK0KKKKKKKKX
XKKXXKXXXXXXXXXXXNNNNNcoNNXXKKO,''''.'......:dxkOOO000k,..''',,lNXKXKKXKKK0KKKXKKKK
KXXKKXXXKXXKXXXXXXXNNNoONNXXX0;'''''''''..'lkkkkkkxxxd'...'''',0N0KKKKKXKKKKKK0XKKK
XXXXXKKXXKXXXXXXXXXXXXOONNNXXl,,;;,;;;;;;;d0K00Okddoc,,,,,,,,,xNNOXKKKKKXKKKKKKKXKK
XXXXXXXXXXXXXXXXXXXXXXXONNNXx;;;;;;;;;,,:xO0KK0Oxdoc,,,,,,,,,oNN0KXXKKXKKXKKKKKKKXK
XKXXKXXXXXXXXXXXXXXXXXXXXWNX:;;;;;;;;;,cO0KKKK0Okxl,,,,,,,,,oNNK0NXXXXXXXXXKKKKKKKX
XXXXXXXXXXXXXXXXXXXXXXXNNNWNc;;:;;;;;;xKXXXXXXKK0x,,,,,,,,,dXNK0NXXXXXXXXXXXKKXKKKK
XKXXXXXXXXXXXXXXXXXXXXNNWWNWd;:::;;;:0NNNNNNNNNXO;,,,,,,,:0NN0XNXNXXXXXXXXXXXKKXKKX
NXXXXXXXXXXXXXXXXXXXXXNNNNNNNl:::;;:KNNNNNNNNNNO;,,,,,,;xNNK0NXNXXNXXXXXXKXXKKKKXKK
XXNNXNNNXXXXXXXXXXXXXNNNNNNNNNkl:;;xWWNNNNNWWWk;;;;;;;xNNKKXNXNXXNXXXXXXXXXXXKXKKXK
XXXXXNNNNXNNNNXXXXXXNNNNNNNNNNNNKkolKNNNNNNNNx;;;;;lkNNXNNNNXXXNXXNXXXXXXXXXXXKKKKX
XXXXXXXXXXXNNNNNNNNNNNNNNNNNNNNNNNNNKXNNNNWNo:clxOXNNNNNNNNXNXXXXXXXXXXXXXXXKKXKKKK
XXXXNXXXNXXXNXXNNNNNWWWWWNNNNNNNNNNNNNNNNNWWNWWNWNNWNNNNNNNNXXXXXXNXXXXXXXXXXKKXKKX
XNXXXXNNXXNXXNNXNXNWWWWWWWWWNNNNNNNNNNNNNWWWWNNNNNNNNNNNNNNNNNNNNNXNXXXXNXXXXXXKXKK
XXXXNXXNNXXXNXXNXXNWWWNNNNNNNNNWWNNNNNNNNWWWWWWNWNNNNNNNNNNNNNNNXXNXNXXXXNXXXXKXKXK

I need to list files in my home/
To check on project logos
But what I see with ls there,
Are quotes from desert hobos...

which piece of my command does fail?
I surely cannot find it.
Make straight my path and locate that-
I'll praise your skill and sharp wit!

Get a listing (ls) of your current directory.
```

#### Solution
We quickly see that someone has messed with the path.

```
elf@bd2b9636c43a:~$ ls
This isn't the ls you're looking for
elf@bd2b9636c43a:~$ which ls
/usr/local/bin/ls
elf@bd2b9636c43a:~$ echo $PATH
/usr/local/bin:/usr/bin:/bin:/usr/local/games:/usr/games
```
There is a fake `ls` binary in /usr/local/bin. And that directory is first in our path.
As a result, linux will search that path first and find the bad `ls` binary and use it.

We could now fix the path, or just use the correct binary directly.
So we just run `/bin/ls` instead.

```
elf@bd2b9636c43a:~$ /bin/ls
```

That's it. We are done.


-----------------------------
### Nyanshell
#### Context
Initial Dialog:
Alabaster Snowball
> Welcome to the Speaker UNpreparedness Room!
> My name's Alabaster Snowball and I could use a hand.
> I'm trying to log into this terminal, but something's gone horribly wrong.
> Every time I try to log in, I get accosted with ... a hatted cat and a toaster pastry?
> I thought my shell was Bash, *not* flying feline.
> When I try to overwrite it with something else, I get permission errors.
> Have you heard any chatter about immutable files? And what is `sudo -l` telling me?

Completed Dialog:
Alabaster Snowball
> Who would do such a thing??  Well, it IS a good looking cat.
> Have you heard about the Frido Sleigh contest?
> There are some serious prizes up for grabs.
> The content is strictly for elves. Only elves can pass the CAPTEHA challenge required to enter.
> I heard there was a talk at KCII about using machine learning to defeat challenges like this.
> I don't think anything could ever beat an elf though!


Challenge-url:  
https://docker2019.kringlecon.com/?challenge=nyanshell

Location:  
Speaker UNpreparedness Room


#### MOTD
When we start the terminal, we are greeted with the following message:
```
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄░░░░░░░░░
░░░░░░░░▄▀░░░░░░░░░░░░▄░░░░░░░▀▄░░░░░░░
░░░░░░░░█░░▄░░░░▄░░░░░░░░░░░░░░█░░░░░░░
░░░░░░░░█░░░░░░░░░░░░▄█▄▄░░▄░░░█░▄▄▄░░░
░▄▄▄▄▄░░█░░░░░░▀░░░░▀█░░▀▄░░░░░█▀▀░██░░
░██▄▀██▄█░░░▄░░░░░░░██░░░░▀▀▀▀▀░░░░██░░
░░▀██▄▀██░░░░░░░░▀░██▀░░░░░░░░░░░░░▀██░
░░░░▀████░▀░░░░▄░░░██░░░▄█░░░░▄░▄█░░██░
░░░░░░░▀█░░░░▄░░░░░██░░░░▄░░░▄░░▄░░░██░
░░░░░░░▄█▄░░░░░░░░░░░▀▄░░▀▀▀▀▀▀▀▀░░▄▀░░
░░░░░░█▀▀█████████▀▀▀▀████████████▀░░░░
░░░░░░████▀░░███▀░░░░░░▀███░░▀██▀░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░

nyancat, nyancat
I love that nyancat!
My shell's stuffed inside one
Whatcha' think about that?

Sadly now, the day's gone
Things to do!  Without one...
I'll miss that nyancat
Run commands, win, and done!

Log in as the user alabaster_snowball with a password of Password2, and land in a Bash prompt.

Target Credentials:

username: alabaster_snowball
password: Password2
```

#### Solution
If we just try to `su` to alabaster_snowball, we see something very unexpected happen:
![NYAN-NYAN-NYAN](images/nyanshell.png)


We look at '/etc/passwd' to see what shell is being loaded for alabaster snowball:

```
elf@1fd924a3fa2c:~$ cat /etc/passwd
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
_apt:x:100:65534::/nonexistent:/usr/sbin/nologin
elf:x:1000:1000::/home/elf:/bin/bash
alabaster_snowball:x:1001:1001::/home/alabaster_snowball:/bin/nsh
```

We notice that alabaster_snowball is running the strange shell `/bin/nsh`
if we look at this shell we see its permissions and notice that we should be able to overwrite it.
However, if we actually try, we get a permission denied

```
elf@1fd924a3fa2c:~$ ls -la /bin/nsh
-rwxrwxrwx 1 root root 75680 Dec 11 17:40 /bin/nsh
elf@1fd924a3fa2c:~$ echo '' > /bin/nsh
-bash: /bin/nsh: Operation not permitted
```
Looking at `sudo -l` we see that we are only allowed to run one specific command as root:
```
elf@1fd924a3fa2c:~$ sudo -l
Matching Defaults entries for elf on 1fd924a3fa2c:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

User elf may run the following commands on 1fd924a3fa2c:
    (root) NOPASSWD: /usr/bin/chattr
```
So we can run `chattr`
The `chattr` command is used to change file attributes on a Linux file system.
Lets have a look at the current attributes for `/bin/nsh`

```
elf@1fd924a3fa2c:~$ lsattr /bin/nsh
----i---------e---- /bin/nsh
```

We see that the immutable flag is set. That is why we cannot overwrite the file.
We can however use the `chattr` command to remove this flag ourself.

```
elf@1fd924a3fa2c:~$ sudo /usr/bin/chattr -i /bin/nsh
elf@1fd924a3fa2c:~$ lsattr /bin/nsh
--------------e---- /bin/nsh
```

Indeed, now we can overwrite the shell. So we just overwrite it with the real bash shell and we are ready.
We then just `su` to alabaster_snowball with the provided credentials and we are done.

```
elf@1fd924a3fa2c:~$ cp /bin/bash /bin/nsh
elf@1fd924a3fa2c:~$ su alabaster_snowball
Password:
Loading, please wait......


You did it! Congratulations!
```

That's all there is to this challenge!

-----------------------------
### Mongo Pilfer
#### Context
Initial Dialog:
Holly Evergreen
> Hey! It's me, Holly Evergreen! My teacher has been locked out of the quiz database and can't remember the right solution.
> Without access to the answer, none of our quizzes will get graded.
> Can we help get back in to find that solution?
> I tried `lsof -i`, but that tool doesn't seem to be installed.
> I think there's a tool like `ps` that'll help too.  What are the flags I need?
> Either way, you'll need to know a teensy bit of Mongo once you're in.
> Pretty please find us the solution to the quiz!

Completed Dialog:
Holly Evergreen
> Woohoo! Fantabulous! I'll be the coolest elf in class.
> On a completely unrelated note, digital rights management can bring a hacking elf down.
> That ElfScrow one can really be a hassle.
> It's a good thing Ron Bowes is giving a talk on reverse engineering!
> _That_ guy knows how to rip a thing apart.  It's like he *breathes* opcodes!


Challenge-url:  
https://docker2019.kringlecon.com/?challenge=mongo


Location:  
netwars (NetWars)


#### MOTD
When we start the terminal, we are greeted with the following message:
```
'...',...'::'''''''''cdc,',,,,,,,cxo;,,,,,,,,:dl;,;;:;;;;;l:;;;cx:;;:::::lKXkc::
oc;''.',coddol;''';ldxxxxoc,,,:oxkkOkdc;,;:oxOOOkdc;;;:lxO0Oxl;;;;:lxOko::::::cd
ddddocodddddddxxoxxxxxkkkkkkxkkkkOOOOOOOxkOOOOOOO00Oxk000000000xdk00000K0kllxOKK
coddddxxxo::ldxxxxxxdl:cokkkkkOkxl:lxOOOOOOOkdlok0000000Oxok00000000OkO0KKKKKKKK
'',:ldl:,'''',;ldoc;,,,,,,:oxdc;,,,;;;cdOxo:;;;;;:ok0kdc;;;;:ok00kdc:::lx0KK0xoc
oc,''''';cddl:,,,,,;cdkxl:,,,,,;lxOxo:;;;;;:ldOxl:;;:;;:ldkoc;;::;;:oxo:::ll::co
xxxdl:ldxxxxkkxocldkkkkkkkkocoxOOOOOOOkdcoxO000000kocok000000kdccdk00000ko:cdk00
oxxxxxxxxkddxkkkkkkkkkdxkkkkOOOOOOxOOOOO00OO0Ok0000000000OO0000000000O0000000000
',:oxkxoc;,,,:oxkkxo:,,,;ldkOOkdc;;;cok000Odl:;:lxO000kdc::cdO0000xoc:lxO0000koc
l;'',;,,,;lo:,,,;;,,;col:;;;c:;;;col:;;:lc;;:loc:;:co::;:oo:;;col:;:lo:::ldl:::l
kkxo:,:lxkOOOkdc;;ldOOOOOkdc;:lxO0000ko:;:oxO000Oxl::cdk0000koc::ox0KK0ko::cok0K
kkkkOkOOOOOkOOOOOOOOOOOOOOOOOO0000000000O0000000000000000000000O000KKKKKK0OKKKKK
,:lxOOOOxl:,:okOOOOkdl;:lxO0000Oxl:cdk00000Odlcok000000koclxO00000OdllxOKKKK0kol
l;,,;lc;,,;c;,,;lo:;;;cc;;;cdoc;;;l:;;:oxoc::cc:::lxxl:::l:::cdxo:::lc::ldxoc:cl
KKOd:,;cdOXXXOdc;;:okKXXKko:;;cdOXNNKxl:::lkKNNXOo:::cdONNN0xc:::oOXNN0xc::cx0NW
XXXXX0KXXXXXXXXXK0XXXXXXNNNX0KNNNNNNNNNX0XNNNNNNNNN0KNNNNNNNNNK0NNNNNNNWNKKWWWWW
:lxKXXXXXOdcokKXXXXNKkolxKNNNNNN0xldOXNNNNNXOookXNNNNWN0xokKNNNNNNKxoxKWWNWWXOod
:;,,cdxl;,;:;;;cxOdc;;::;;:dOOo:;:c:::lk0xl::cc::lx0ko:::c::cd0Odc::c::cx0ko::lc
OOxl:,,;cdk0Oxo:;;;:ok00Odl:;;:lxO00koc:::ldO00kdl:::cok0KOxl:::cok0KOxl:::lx0KK
00000kxO00000000OxO000000000kk000000000Ok0KK00KKKK0kOKKKKKKKK0kOKKKKKKKK0k0KKKKK
:cok00000OxllxO000000koldO000000Odlok0KKKKKOxoox0KKKKK0koox0KKKKK0xoox0KKKKKkdld
;:,,:oxoc;;;;;;cokdl:;;:;;coxxoc::c:::lxkdc::c:::ldkdl::cc::ldkdl::lc::lxxoc:loc
OOkdc;;;:oxOOkoc;;;:lxO0Odl:;::lxO00koc:::lxO00kdl:::lxO00Odl::cox0KKOdl:cox0KK0
OOOOOOxk00000000Oxk000000000kk000000000Ok0KK0000KK0k0KKKKKKKK0OKKKKKKKKK00KKK0KK
c:ldOOOO0Oxoldk000000koldk000000kdlox0000K0OdloxOKK0K0kdlox0KKKK0xocok0KKK0xocld
;l:;;cooc;;;c:;:lddl:;:c:::ldxl:::lc::cdxo::coc::cddl::col::cddl:codlccldlccoxdc
000Odl;;:ok000koc;;cok0K0kdl::cdk0KKOxo::ldOKKK0xoccox0KKK0kocldOKKKK0xooxOKKKKK
0000000O0000000000O0KKK0KKKK00KKKK0KKKKK0KKKK0KKKKKKKKKK0KKKKKKKKKO0KKKKKKKKOkKK
c::ldO000Oxl:cok0KKKOxl:cdk0KKKOdl:cok0KK0kdl:cok0KK0xoccldk0K0kocccldOK0kocccco
;;;;;;cxl;;;;::::okc::::::::dxc::::::::odc::::::::ol:ccllcccclcccodocccccccdkklc

Hello dear player!  Won't you please come help me get my wish!
I'm searching teacher's database, but all I find are fish!
Do all his boating trips effect some database dilution?
It should not be this hard for me to find the quiz solution!

Find the solution hidden in the MongoDB on this system.
```


#### Solution
We start by trying to connect to the mongo database

```
elf@de490e548003:~$ mongo
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017
2019-12-17T15:00:26.355+0000 W NETWORK  [thread1] Failed to connect to 127.0.0.1:27017, in(checking socket for error after poll), reason: Connection refused
2019-12-17T15:00:26.356+0000 E QUERY    [thread1] Error: couldn't connect to server 127.0.0.1:27017, connection attempt failed :
connect@src/mongo/shell/mongo.js:251:13
@(connect):1:6
exception: connect failed


Hmm... what if Mongo isn't running on the default port?
```

It seems that we need to find the port mongo is listening on.
We can do this by running the following command:

```
elf@de490e548003:~$ ps aux
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
elf          1  0.0  0.0  18508  3496 pts/0    Ss   14:53   0:00 /bin/bash
mongo        9  0.5  0.0 1016780 59484 ?       Sl   14:53   0:02 /usr/bin/mongod --quiet --fork --port 12121 --bind_ip 127.0.0.1 --logpath=/tmp/mongo.log
elf         54  0.0  0.0  34400  2928 pts/0    R+   15:01   0:00 ps aux
```
Alternatively, we could have checked out `sudo -l`
```
elf@de490e548003:~$ sudo -l
User elf may run the following commands on de490e548003:
    (mongo) NOPASSWD: /usr/bin/mongod --quiet --fork --port 12121 --bind_ip 127.0.0.1 --logpath\=/tmp/mongo.log
    (root) SETENV: NOPASSWD: /usr/bin/python /updater.py
```
In either case, we see that there is a mongo process running with the port flag 12121.
We connect to it and look around:
```
elf@de490e548003:/tmp$ mongo localhost:12121
MongoDB shell version v3.6.3
connecting to: mongodb://localhost:12121/test
MongoDB server version: 3.6.3
Welcome to the MongoDB shell.
For interactive help, type "help".
For more comprehensive documentation, see
        http://docs.mongodb.org/
Questions? Try the support group
        http://groups.google.com/group/mongodb-user
Server has startup warnings:
2019-12-17T14:53:59.109+0000 I CONTROL  [initandlisten]
2019-12-17T14:53:59.109+0000 I CONTROL  [initandlisten] ** WARNING: Access control is not enabled for the database.
2019-12-17T14:53:59.109+0000 I CONTROL  [initandlisten] **          Read and write access to data and configuration is unrestricted.
2019-12-17T14:53:59.109+0000 I CONTROL  [initandlisten]
2019-12-17T14:53:59.109+0000 I CONTROL  [initandlisten]
2019-12-17T14:53:59.109+0000 I CONTROL  [initandlisten] ** WARNING: /sys/kernel/mm/transparent_hugepage/enabled is 'always'.
2019-12-17T14:53:59.109+0000 I CONTROL  [initandlisten] **        We suggest setting it to 'never'
2019-12-17T14:53:59.109+0000 I CONTROL  [initandlisten]
> show dbs
admin   0.000GB
config  0.000GB
elfu    0.000GB
local   0.000GB
test    0.000GB
> use elfu
switched to db elfu
> show collections
bait
chum
line
metadata
solution
system.js
tackle
tincan
```

We see the interesting looking database 'solution'.

```
> db.solution.find()
{ "id" : "You did good! Just run the command between the stars: ** db.loadServerScripts();displaySolution(); **" }
```
Well, it seems like we did it, so lets just run that final command.
```
db.loadServerScripts();displaySolution();
```

And we are done.


-----------------------------
### Smart Braces
#### Context
Initial Dialog:
Kent Tinseltooth
> OK, this is starting to freak me out!
> Oh sorry, I'm Kent Tinseltooth.  My Smart Braces are acting up.
> Do...  Do you ever get the feeling you can hear things?  Like, voices?
> I know, I sound crazy, but ever since I got these...  Oh!
> Do you think you could take a look at my Smart Braces terminal?
> I'll bet you can keep other students out of my head, so to speak.
> It might just take a bit of Iptables work.

Completed Dialog:
Kent Tinseltooth
> Oh thank you!  It's so nice to be back in my own head again.  Er, alone.
> By the way, have you tried to get into the crate in the Student Union?  It has an interesting set of locks.
> There are funny rhymes, references to perspective, and odd mentions of eggs!
> And if you think the stuff in your browser looks strange, you should see the page source...
> Special tools?  No, I don't think you'll need any extra tooling for those locks.
> BUT - I'm pretty sure you'll need to use Chrome's developer tools for that one.
> Or sorry, you're a Firefox fan?
> Yeah, Safari's fine too - I just have an ineffible hunger for a physical Esc key.
> Edge?  That's cool.  Hm?  No no, I was thinking of an unrelated thing.
> Curl fan?  Right on!  Just remember: the Windows one doesn't like double quotes.
> _Old school, huh?  Oh sure - I've got what you need right here..._


Challenge-url:  
https://docker2019.kringlecon.com/?challenge=iptables

Location:  
Student Union


#### MOTD
When we start the terminal, we are greeted with the following message (I added an image rahter than a transcript to preserve the coloring here):
![Smart braces motd](images/smart_braces_motd.png)

#### Solution
This challenge is timed. You need to complete the iptables rules within 5 minutes. Note that there is nothing stopping you from trying multiple times. So the time limitation is not much of a problem.
```
elfuuser@e8bce7331ea7:~$ cat /home/elfuuser/IOTteethBraces.md 
# ElfU Research Labs - Smart Braces
### A Lightweight Linux Device for Teeth Braces
### Imagined and Created by ElfU Student Kent TinselTooth

This device is embedded into one's teeth braces for easy management and monitoring of dental status. It uses FTP and HTTP for management and monitoring purposes but also has SSH for remote access. Please 
refer to the management documentation for this purpose.

## Proper Firewall configuration:

The firewall used for this system is `iptables`. The following is an example of how to set a default policy with using `iptables`:

> sudo iptables -P FORWARD DROP

The following is an example of allowing traffic from a specific IP and to a specific port:

> sudo iptables -A INPUT -p tcp --dport 25 -s 172.18.5.4 -j ACCEPT


A proper configuration for the Smart Braces should be exactly:

1. Set the default policies to DROP for the INPUT, FORWARD, and OUTPUT chains.
2. Create a rule to ACCEPT all connections that are ESTABLISHED,RELATED on the INPUT and the OUTPUT chains.
3. Create a rule to ACCEPT only remote source IP address 172.19.0.225 to access the local SSH server (on port 22).
4. Create a rule to ACCEPT any source IP to the local TCP services on ports 21 and 80.
5. Create a rule to ACCEPT all OUTPUT traffic with a destination TCP port of 80.
6. Create a rule applied to the INPUT chain to ACCEPT all traffic from the lo interface.
```

Let's implement these rules.

```
elfuuser@e8bce7331ea7:~$ sudo iptables -P INPUT DROP
elfuuser@e8bce7331ea7:~$ sudo iptables -P FORWARD DROP
elfuuser@e8bce7331ea7:~$ sudo iptables -P OUTPUT DROP

elfuuser@e8bce7331ea7:~$ sudo iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
elfuuser@e8bce7331ea7:~$ sudo iptables -A OUTPUT -m state --state ESTABLISHED,RELATED -j ACCEPT

elfuuser@e8bce7331ea7:~$ sudo iptables -A INPUT -p tcp -s 172.19.0.225 --dport 22 -j ACCEPT
elfuuser@e8bce7331ea7:~$ sudo iptables -A OUTPUT -p tcp -d 172.19.0.225 --sport 22 -j ACCEPT

elfuuser@e8bce7331ea7:~$ sudo iptables -A INPUT -p tcp -m multiport --dports 21,80 -j ACCEPT
elfuuser@e8bce7331ea7:~$ sudo iptables -A OUTPUT -p tcp -m multiport --sports 21,80 -j ACCEPT

elfuuser@e8bce7331ea7:~$ sudo iptables -A OUTPUT -p tcp --dport 80 -j ACCEPT

elfuuser@e8bce7331ea7:~$ sudo iptables -A INPUT -i lo -j ACCEPT
```
We now wait a couple seconds for the background task to verify our rules and we are done.


NOTE:
> There seemed to be some small issues with this challenge where if you did not allow the MOTD to slowly play out, it would no longer properly verify your rules later.


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
