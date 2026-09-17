from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

BOT_TOKEN = '8295968916:AAHzSPv7DDE-Zx1QAyYB-EPjOi7NxdZyM9M'

CONTENT = {
    'kali': """🐉 Kali Linux

Kali Linux is a Debian-based Linux distribution created by Offensive Security for security auditing, penetration testing, network research and digital forensics.

Unlike traditional operating systems, Kali is not designed for everyday use. It is a specialized tool built for cybersecurity specialists and ethical hackers.

⚡ Main advantage:
Kali comes fully ready with 600+ pre-installed security tools. It can run from USB, in Virtual Machines, on Raspberry Pi, or inside Windows via WSL.

📂 Key categories:
🕵️ Information Gathering: Nmap, Maltego
🌐 Web Security: Burp Suite, SQLmap
🎯 Exploitation: Metasploit
🔑 Password Attacks: Hashcat, John the Ripper
📶 Wireless: Aircrack-ng
🔬 Forensics: Autopsy, Volatility

🎓 Industry standard for OSCP and CEH certifications.""",

    'trojan': """☠️ Trojan (Trojan Horse)

A Trojan is malware that disguises itself as legitimate software to trick the user into installing it.

Unlike viruses or worms, Trojans cannot self-replicate. They require human action.

📂 Types:
🚪 Remote Access Trojans (RAT): Full hidden control
🔑 Keyloggers: Record every keystroke
🏦 Banking Trojans: Steal financial data
🤖 Botnet Trojans: Turn PC into zombie
📦 Droppers: Download more malware

🛡️ Protection:
Don't download from shady sources
Don't open suspicious attachments
Use reliable antivirus
Keep OS updated""",

    'osint': """🔍 OSINT (Open Source Intelligence)

Collection and analysis of information from publicly available sources.

⚡ What can be found:
📛 Name and surname
🏙️ City/region
🕵️ Connections to other numbers
🔗 Social media accounts
📅 Registration date in messengers

⚠️ Important notes:
Data may be inaccurate
Legal aspect: may violate laws (GDPR)
Some services are paid

🛠️ Examples:
OSINT Framework
TryHackMe OSINT rooms
Bellingcat guides

🎓 Learn legally and respect privacy.""",

    'hacking': """💻 Hacking

Types of hackers:
🟢 White Hat - Ethical hackers
🔴 Black Hat - Illegal hackers
⚪ Grey Hat - No malicious intent
🏴 Hacktivist - Political goals

⚡ Main directions:
🌐 Web Security
📡 Network Security
🧠 Social Engineering
🎣 Phishing
📱 Mobile Security

🛡️ Ethical Hacking (Pentesting)
Companies hire hackers to test their systems.

How to start:
🐧 Learn Linux
🐍 Learn Python, Bash
🌍 Understand networks
🏋️ Practice legally:
- Hack The Box
- TryHackMe
- PortSwigger Academy

⚠️ IMPORTANT: Hacking without permission is a crime.""",

    'ddos': """💥 DDoS (Distributed Denial of Service)

A DDoS attack creates huge traffic to block a website or server.

Imagine a small shop where a thousand fake people try to enter at once. Real customers can't get in.

⚡ How it works:
Uses botnets - networks of infected devices controlled by attackers.

📂 Main types:
🌊 Volumetric Attacks
🔌 Protocol Attacks
🌐 Application Layer Attacks

🛡️ Protection:
- Cloudflare
- Akamai
- AWS Shield""",

    'virus': """🦠 Computer Virus for Windows

A virus is malware that self-replicates and injects code into legitimate files (.exe, .dll).

⚡ How it works:
📥 Infection: User runs infected file
💣 Payload: Can damage or encrypt data
💽 Propagation: Can spread through removable media and shared files

📂 Types:
🚀 File Viruses
👢 Boot Viruses
📜 Macro Viruses
👻 Polymorphic Viruses

🛡️ Protection:
Antivirus software
Regular OS updates
Don't run suspicious files
Backup important data""",

    'windows': """🪟 Microsoft Windows

World's most popular family of proprietary operating systems by Microsoft. First released in 1985.

⚡ Key features:
🖱️ Friendly GUI
🎮 Gaming support via DirectX
📦 Huge software ecosystem
⚙️ NT Architecture

📂 Architecture:
📝 Windows Registry
📁 NTFS with BitLocker
🐧 WSL - run Linux inside Windows

🛡️ Security:
🔒 Windows Defender
🔒 UAC
🔒 TPM 2.0 + Secure Boot"""
}


def main_keyboard():
    keyboard = [
        [KeyboardButton("🐉 Kali Linux")],
        [KeyboardButton("☠️ Trojan"), KeyboardButton("🔍 OSINT")],
        [KeyboardButton("💻 Hacking"), KeyboardButton("💥 DDoS")],
        [KeyboardButton("🦠 Virus"), KeyboardButton("🪟 Windows")],
        [KeyboardButton("❓ Help")]
    ]

    return ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )


def back_keyboard():
    return ReplyKeyboardMarkup(
        [[KeyboardButton("🔙 Back")]],
        resize_keyboard=True
    )


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔥 INFILTRATION 🔥\n"
        "═══════════════════\n\n"
        "Welcome to Cybersecurity Knowledge Bot\n\n"
        "📚 Choose a topic to learn:",
        reply_markup=main_keyboard()
    )


async def handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip() if update.message.text else ""

    if text == "🐉 Kali Linux":
        await update.message.reply_text(
            CONTENT['kali'],
            reply_markup=back_keyboard()
        )

    elif text == "☠️ Trojan":
        await update.message.reply_text(
            CONTENT['trojan'],
            reply_markup=back_keyboard()
        )

    elif text == "🔍 OSINT":
        await update.message.reply_text(
            CONTENT['osint'],
            reply_markup=back_keyboard()
        )

    elif text == "💻 Hacking":
        await update.message.reply_text(
            CONTENT['hacking'],
            reply_markup=back_keyboard()
        )

    elif text == "💥 DDoS":
        await update.message.reply_text(
            CONTENT['ddos'],
            reply_markup=back_keyboard()
        )

    elif text == "🦠 Virus":
        await update.message.reply_text(
            CONTENT['virus'],
            reply_markup=back_keyboard()
        )

    elif text == "🪟 Windows":
        await update.message.reply_text(
            CONTENT['windows'],
            reply_markup=back_keyboard()
        )

    elif text == "❓ Help":
        await update.message.reply_text(
            "❓ HELP\n"
            "═════════\n\n"
            "📚 Topics:\n"
            "🐉 Kali Linux\n"
            "☠️ Trojan\n"
            "🔍 OSINT\n"
            "💻 Hacking\n"
            "💥 DDoS\n"
            "🦠 Virus\n"
            "🪟 Windows\n\n"
            "⚠️ Important:\n"
            "For educational purposes only.",
            reply_markup=back_keyboard()
        )

    elif text == "🔙 Back":
        await update.message.reply_text(
            "🔥 INFILTRATION 🔥\n"
            "═══════════════════\n\n"
            "📚 Choose a topic:",
            reply_markup=main_keyboard()
        )


def main():
    print("=" * 50)
    print("   INFILTRATION BOT")
    print("=" * 50)

    if not BOT_TOKEN:
        print("❌ ERROR: BOT_TOKEN is empty!")
        print("Add your Telegram bot token to BOT_TOKEN.")
        return

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            handler
        )
    )

    print("✅ BOT STARTED")
    print("=" * 50)

    app.run_polling()


if __name__ == "__main__":
    main()
