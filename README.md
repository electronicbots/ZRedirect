## Introduction

ZRedirect, a simple tool for finding open redirect vulnerability in a website. It works by providing a file contains for example wayback urls.

## Features

ZRedirect will try to bypass the following type:

- Blacklisted Keyword
- Blacklisted Character
- Blacklist Filter
- IP Formats

## Installation

Run the following commands:
```
$ git clone https://github.com/electronicbots/ZRedirect.git
$ pip3 install -r requirements.txt
```

## Usage

![Usage](https://github.com/electronicbots/ZRedirect/blob/main/images/2.png)

## Example

```
python3 ZRedirect.py --target urls.txt
```
