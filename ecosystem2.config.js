module.exports = {
  apps: [
    {
      name: "Switch (BotWA)",
      script: "botcontrol.py",
      interpreter: "python3",
      watch: true,
      ignore_watch: ["node_modules", "logs"],
    },
  ],
};