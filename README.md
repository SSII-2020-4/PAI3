# PAI3
The server and client are developed and should be run in linux machines, specifically in Ubuntu.


## Init project

To init project in linux install `sqlcipher` package, example in Ubuntu:

```bash
# sqlcipher install
sudo apt install sqlcipher libsqlcipher0 libsqlcipher-dev
```

The certificate and private key can be created using the followig command: 
```bash
openssl req -newkey rsa:2048 -keyout key.pem -x509 -days 365 -out certificate.pem
```


## Capture datagramas in diferents networks

First generate certificate to ssh connect, and then:

```bash
ssh user@host tcpdump -U -s0 'port 8443' -w - | wireshark -k -i -
```

## Known issues
#### Python version
To run properly the server and client, you should have installed python 3.8 or higher. To check the python version, use:
```bash 
python --version
```
#### Installing pysqlcipher3
If you have problems when installing the library `pysqlcipher3`, you should be sure that you have installed the python-dev tools. You can install it using the next command:
```bash 
sudo apt-get install pythonx.x-dev
```
where x.x is the version of python you are currently using (in our case, sudo apt-get install python3.8-dev).

