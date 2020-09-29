## Environment
Python 2.7.18

## Preparation
### modules
`pip install thinkgear`
`pip install pyserial`
`pip install dotenv`

### set mindwave port
1. create .env file directly under the project
2. Connect with MindWave via Bluetooth
(mac)
3. ls `/dev/tty.*`
4. Write 5 in .env file (X is the value output by 3)
5. MINDWAVE_PORT = "X"
(windows)
3. Open Device Manager by clicking on the Start menu, then Control Panel, then System, and then Device Manager.
4. Click the [+] next to Ports (COM & LPT) to expand the list of ports on your system.
5. Look for "MindWave USB Adapter (COM NN)", where NN is your COM port number. Use
that number in the game or application.
6. Write 7 in .env file (X is the 5)
7. MINDWAVE_PORT = "X"


## Execute
1. Connect with MindWave via Bluetooth
2. `python2 src/main.py`