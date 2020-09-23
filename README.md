# Telegram-cloud (A.K.A tgcloud)

telegram-cloud - Download and upload files via telegram, Use your telegram account as a free cloud storage.

Uploader, Downloader, Crawler, Bot 50MB limitation bypasser.

  - Upload file upto 1.5GB
  - Download file from every conversation, group, channel, ...
  - Crawling! search by name or caption for a specific file to download it

You can also:
  - Use it for multiple accounts, download from one Telegram account and upload that on another account, there is no difficulty 
  - download files with file_id

This text you see here is *actually* written in Markdown! To get a feel for Markdown's syntax, type some text into the left window and watch the results in the right.

### Hmm what is this?

It's a library for Telegram messenger, which can give you an ability to download, upload, and more options to do with your Telegram account on CLI.

### Installation

telegram-cloud requires [Python3](https://www.python.org/psf-landing/) and [Telethon](https://github.com/LonamiWebs/Telethon) as requirment.

Install the dependencies.

```sh
$ pip3 install -r requirements.txt
```

### Commands

telegram-cloud is currently working with the following commands. 

| args | help |
| ------ | ------ |
| --mode / -m | Two modes for specify what you want, Available modes: download - upload |
| --name / -n | A Name you choose while tglogin-ing and use for specify the current user you work on it |
| --username / -u | Target username that you want to send file, type 'me' if you want to get it on your 'saved messages' |
| --path / -p | For download mode: pass simple directory path like "/Users/nima/Desktop/Iwanttoescapefrom/"|
| --path / -p | For upload mode: pass file path like "/Users/nima/Desktop/Iwanttoescapefrom/Iran.zip"|
| --caption / -c | For download mode: pass the name of file or caption to crawl and download|
| --caption / -c | For upload mode: write the caption to see it under your file |


### Need more examples?

Download a music from my saved messages and save it on /Users/nima/Desktop/:
```sh
$ tgcloud -m download -n nima -u me -p "/Users/nima/Desktop/" -c "sad but true"
```

Upload a banner with caption to my saved messages :
```sh
$ tgcloud -m upload -n nima -u me -p "/Users/nima/Desktop/banner.png" -c "This is a caption under banner"
```

(optional) Third:
```sh
$ karma test
```
#### Building for source
For production release:
```sh
$ gulp build --prod
```
Generating pre-built zip archives for distribution:
```sh
$ gulp build dist --prod
```
### Docker
Dillinger is very easy to install and deploy in a Docker container.

By default, the Docker will expose port 8080, so change this within the Dockerfile if necessary. When ready, simply use the Dockerfile to build the image.

```sh
cd dillinger
docker build -t joemccann/dillinger:${package.json.version} .
```
This will create the dillinger image and pull in the necessary dependencies. Be sure to swap out `${package.json.version}` with the actual version of Dillinger.

Once done, run the Docker image and map the port to whatever you wish on your host. In this example, we simply map port 8000 of the host to port 8080 of the Docker (or whatever port was exposed in the Dockerfile):

```sh
docker run -d -p 8000:8080 --restart="always" <youruser>/dillinger:${package.json.version}
```

Verify the deployment by navigating to your server address in your preferred browser.

```sh
127.0.0.1:8000
```

#### Telethon + Python
[![Python](https://www.python.org/static/community_logos/python-powered-w-200x80.png)](https://www.python.org/psf-landing/)
See [Telethon](https://github.com/LonamiWebs/Telethon)

### Todos

 - Upload and download multiple files
 - Upload and download a directory
 - Make compatible with windows

### Hmm.. 

