# PAI3
El certificado se puede generar usando el siguiente comando: openssl req -newkey rsa:2048 -keyout key.pem -x509 -days 365 -out certificate.pem



## Init project

To init project in linux install `sqlcipher` package, example in Ubuntu:

```bash
# sqlcipher install
sudo apt install sqlcipher libsqlcipher0 libsqlcipher-dev
```





## Capture datagramas in diferents networks

First generate certificate to ssh connect, and then:

```bash
ssh user@host tcpdump -U -s0 'port 8443' -w - | wireshark -k -i -
```

