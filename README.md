# mell
An automated process to generate Mellanox switch configurations.



# Installation:

This application runs in docker!!!!!!

```
% git clone https://github.com/xod442/Mellon.git
% cd Mellon
Mellon%  docker-compose up -d
```



# Home Screen Form
The home screen form will contain the fields for all variables needed to
complete the switch configuration. Config files for both switches will be
downloaded to the mellon directory. There is also an option to use the CSV
file and bulk import the variables. The configuration files will be saved
in the mellon directory.

You can use
```
configuration text fetch vrf mgmt scp://<user>@<ip-host>/<location of mellon directory>/<config file name>
```

Then issue the apply command

```
configuration text file <name fo config file> apply
```

Either method will work. Look at me..I'm giving you choices!


# Open browser
Use: localhost:5005
