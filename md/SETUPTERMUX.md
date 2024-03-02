# Setup Termux to Connect EC2

```
pkg update && pkg upgrade
pkg install git openssh
```

Open the downloaded keypair, termux will start a new session with the directory keypair is in.
Or you can put keypair on github and clone the repository in termux, and `cd your-repo-name`

- In Connect to Instance, go to SSH Client tab. Follow the instruction and copy the command to termux.

You are now successfully connected. [Go back to GuideAWS](GUIDE-AWS.md)
