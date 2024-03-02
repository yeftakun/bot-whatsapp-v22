# How to Deploy on AWS EC2 Instance

## Create VPC

[Go to VPC Dashboard](https://ap-southeast-1.console.aws.amazon.com/vpcconsole/home?region=ap-southeast-1#Home:) and *Create VPC*

- Select **VPC and more**
- Insert name: mybot-vpc
- IPv4 CIDR Block: `10.0.0.0/16`
- IPv6 CIDR Block: No
- Tenancy: Default
- Number of AZs: 1
- Num of public subnet: 1
- Num of private subnet: 1
- Customize subnet CIDR blocks. Public:`10.0.0.0/24` | Private:`10.0.1.0/24`
- NAT gateways: None
- VPC endpoints: S3 Gateway
- DNS option: Enable DNS hostnames & DNS resolution
- **Create VPC**

## Create EC2 Instance

[Go to EC2 Dashboard](https://ap-southeast-1.console.aws.amazon.com/ec2/home?region=ap-southeast-1#Home:), and **Launch Instance**.

- Name&Tags: mybot-server-1
- Aplication & Software Image: Amazon Linux
- Amazon Machine Image: Amazon Linux 2023 AMI *(free tier)*
- Instance type: t2.micro
- Key Pair login: Create new -> mybot-keypair -> create and download to your local.

**Network Settings (Edit)**

- VPC: mybot-vpc
- Subnet: select public subnets
- Auto-assign public IP: Enable
- Firewall (Security group): Create new *(lol i forgot to create it before this section)*
- SG name: mybot-sg
- Description Default
- Inbound SG Rules 1. type:**ssh** | source type:**Anywhere**
- Add SG Rule
- Inbound SG Rules 2. type:**http** | source type: **Anywhere**
- **Launch Instance**

## Connect to Instance

- In the EC2 Dashboard, go to Instance > your instance > connect > tab EC2 Instance Connect > Connect using EC2 Instance Connect > **Connect**

*You can use termux to connect it. [Here to setup](SETUPTERMUX.md)*

## Install & Setup on EC2 Instance

**Install**
```
sudo yum update -y
sudo yum install -y nodejs
sudo yum install git -y
sudo npm install -g pm2
node -v
npm -v
git --version
```
**Setup**
```
git clone https://github.com/yeftakun/BotWA.git
cd BotWA
npm install
npm start
```
- Insert your phone number for Bot
- Tap the notification on your phone to linked device, insert the code
- Bot has running, but will stoped when your terminal session closed. `ctrl+c` to terminate bot.
```
pm2 start npm -- start
pm2 save
pm2 startup
```
Follow the instructions and the Bot is ready. Now to stop/start the bot, you just need to start/stop the instance. For more practicality, download [AWS Console](https://play.google.com/store/apps/details?id=com.amazon.aws.console.mobile)
<p align="center">
<img src="lv_0_20240202125332.gif" width=60% />
</p>

[Back to Repo](https://github.com/yeftakun/BotWA)
