## Environment
Python 2.7.16-bit

## Preparation
### module
`pip2 install thinkgear`
`pip2 install pyserial`

### set mindwave port
1. create .env file directly under the project
2. Connect with MindWave via Bluetooth
3. `/dev/tty.*`
4. Write 5 in .env file (X is the value output by 3)
5. MINDWAVE_PORT = "X"

## Execute
1. Connect with MindWave via Bluetooth
2. `python2 src/main.py`