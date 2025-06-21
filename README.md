<h1 align="center">🛡️ Open Port Scanner</h1>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=22&pause=1000&color=36FFC6&center=true&vCenter=true&width=600&lines=Cybersecurity+Toolset+Module;Port+Scanner+in+Python+%7C+Threaded+%26+Fast;Scan+%7C+Analyze+%7C+Secure" alt="Typing SVG" />
</p>

---

## 👨‍💻 Developed For

- **Name**: Naveen Kumar  
- **Company**: CODTECH IT SOLUTIONS  
- **ID**: CT12DS2531  
- **Domain**: 🛡️ Cyber Security  
- **Mentor**: Neela Santosh Kumar  

---

## 🕵️‍♂️ Project Brief: *Reconnaissance Starts Here*

Port scanning is one of the **first steps in penetration testing** — it reveals what services are running and potentially vulnerable.

This Python-based **Open Port Scanner** helps security analysts and ethical hackers **enumerate live ports** on a given host, providing vital insights for deeper assessment.

> 🎯 **Purpose**: Identify exposed TCP ports that may serve as entry points for attackers.

---

## 🛠️ Technologies & Tactics

| Component         | Role in Cyber Ops                      |
|------------------|----------------------------------------|
| 🐍 Python         | Language used to code the scanner       |
| 🔌 socket         | Simulates TCP handshakes with targets   |
| ⚔️ threading      | Concurrent scanning – faster footprint  |
| ⏱️ timeout        | Evades slow responses during recon      |

---

## 🧰 Tactical Features

### 🔍 Target Recon
- Scan any IP or domain for open **TCP ports**
- Select your **range of interest** (e.g. `1-1000`)

### 🚀 Multithreaded Deployment
- Leverages **Python threads** for simultaneous port checks
- Faster reconnaissance, smaller time window for detection

### 🎛 Configurable Timeout
- Avoid wasting time on filtered/firewalled ports
- **Set your scanning speed** with a single parameter

### 🧪 Input Sanitation
- Validates IP/Domain format
- Prevents invalid scan range usage

---
📊 Sample Output
bash
Copy
Edit
- [+] Scanning Target: 192.168.1.1
- [✓] Port 22 is open (SSH)
-[✓] Port 80 is open (HTTP)
- [✓] Port 443 is open (HTTPS)
- Scan complete.

---

## ⚙️ Usage Instructions

```bash
python3 port_scanner.py <target> <start_port> <end_port>
