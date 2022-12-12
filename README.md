# Booking web application

https://booking.craftstudios.shop/

## Architecture

- Booking is a django web app with standard static templating running on apache as a web server.
- Apache proxies requests to the standard WSGI application which invokes the Booking application itself.
- There is no decoupling of the front end.
- The continuous delivery pipeline is triggered by a git push to origin by any member that has write access to this repo.
- The git push triggers a webhook where both github and jenkins are listening on in order to build the jenkins pipeline.
- Specifications of the Jenkinsfile can be found above.
- Any push to origin will trigger both webhooks however jenkins will only build the source code located in the "master" branch.

<p align="center" width="100%">
    <img width="90%" src="https://github.com/hupratt/booking/blob/master/arch.drawio.png?raw=true">
</p>

## Features

- [x] Feature 1
- [x] Feature 2
- [x] Feature 3

## Next steps
