# Cyber Network Scanner / Кибер Сетевой Сканер

## Описание / Description

**RU:**  
Этот проект - консольный сетевой сканер, позволяющий выявлять устройства в локальной сети, открытые порты и потенциальные риски.  
Проект написан на Python с использованием Scapy и Nmap. Основная цель - демонстрация навыков в области кибербезопасности и создания модульного сканера.

**EN:**  
This project is a console-based network scanner that identifies devices on a local network, detects open ports, and evaluates potential risks.  
The project is written in Python using Scapy and Nmap. The main goal is to showcase cybersecurity skills and build a modular scanning tool.

---

## Функции / Features

**RU:**
- ARP-сканирование сети (IP и MAC адреса)  
- Сканирование портов с использованием Nmap (открытые/фильтрованные)  
- Определение типа устройства по баннерам сервисов (banner grabbing)  
- Анализ рисков и рекомендации по закрытию уязвимых портов  
- Читаемый вывод в терминале, включая IP, MAC, устройство, открытые порты и риски  
- Модульная структура: легко расширять сканеры и правила анализа  

**EN:**
- ARP network scanning (IP and MAC addresses)  
- Port scanning using Nmap (open/filtered ports)  
- Device type detection via service banner grabbing  
- Risk analysis with recommendations for securing vulnerable ports  
- Readable CLI output including IP, MAC, device type, open ports, and risks  
- Modular structure: easy to extend scanners and analysis rules  

---

## Требования / Requirements

**RU:**
- Python 3.x  
- Библиотеки: `scapy`, `python-nmap`, `requests` (если используется)  
- Установленный Nmap  
- Linux рекомендуется, Windows поддерживается ограниченно  

**EN:**
- Python 3.x  
- Libraries: `scapy`, `python-nmap`, `requests` (if used)  
- Nmap installed  
- Linux recommended, Windows support is limited  

---

## Установка / Installation

**RU:**
- Клонируйте репозиторий:  
```bash```
- git clone <URL вашего репозитория>
Перейдите в папку проекта и создайте виртуальное окружение:
- python3 -m venv venv
- source venv/bin/activate  # Linux
- venv\Scripts\activate     # Windows

Установите зависимости:
- pip install -r requirements.txt
- Убедитесь, что Nmap установлен и доступен из командной строки.

**EN:**
Clone the repository:
```bash```
- git clone <Your repository URL>
Navigate to the project folder and create a virtual environment:
- python3 -m venv venv
- source venv/bin/activate  # Linux
- venv\Scripts\activate     # Windows

- Install dependencies:
- pip install -r requirements.txt
- Make sure Nmap is installed and available in the command line.

---

## Использование / Usage
- python main.py

---

## Примечания / Notes

**RU:**
- Device detection реализован только через banner grabbing и MAC OUI.
- Расширение возможностей возможно через добавление новых сканеров и правил анализа.
- CLI-версия проекта работает на Linux, Windows поддерживается частично.

**EN:**
- Device detection is implemented using banner grabbing and MAC OUI only.
- Functionality can be extended by adding new scanners and analysis rules.
- The CLI version works on Linux, Windows support is partial.

---

## Лицензия / License
-MIT License
