# Loading in instagram

The script downloads photos from the Spacex and Hubble 
services and uploads them to the Instagram account. 

## Getting Started

### Manual Installation

1. **Clone the repository:**

```bash
https://github.com/5p1K3-wq/loading_in_instagram.git
```
2. **Open directory:**

`cd loading_in_instagram/`

3. Run a script

```bash
python3 main.py -u username -p password -proxy https://localhost:8080

-u - login from instagram account
-p - passoword from instagram account
-proxy - proxy server
```

## Built With

[Pillow 7.1.2](https://pypi.org/project/Pillow/) - Image Library

[instabot 0.117.0](https://pypi.org/project/instabot/) - Free Instagram python bot

[argparse 1.4.0](https://pypi.org/project/argparse/) - The argparse module makes it easy to write user friendly command 
line interfaces.