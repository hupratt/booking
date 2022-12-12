# Booking web application

https://booking.craftstudios.shop/

## Architecture

- Booking is a django web app with standard static templating running on apache as a web server.
- Apache proxies requests to the standard WSGI application which invokes the Booking application itself.
- There is no decoupling of the front end.
- A load balancer sitting in front of the servers distributes tasks using a round robin scheduler. This setup mitigates timeouts and ensures failover as there is always a server that can handle incoming requests without having to upgrade to a more expensive tier with our cloud provider. Further improvements to the set up will include: delegating caching to the load balancer and request compression
- The continuous delivery pipeline is triggered by a git push to origin by any member that has write access to this repo.
- The git push triggers a webhook where both github and jenkins are listening on in order to build the jenkins pipeline.
- Specifications of the Jenkinsfile can be found above.
- Any push to origin will trigger both webhooks however jenkins will only build the source code located in the "master" branch.

<img src="[/path/to/img.jpg](https://viewer.diagrams.net/?tags=%7B%7D&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Untitled%20Diagram.drawio#R1ZbbbqMwEIafJpeNACeQXIZD2khdbbdRVe1V5IIDVgymttOkffodF5Nwqra73WNyAf5nzIz9f1iMUJAfLwUus088IWzkWMlxhMKR49hoasFFK8%2BV4iGnElJBE5N0Ftb0hRjRzEv3NCGylag4Z4qWbTHmRUFi1dKwEPzQTtty1q5a4pT0hHWMWV%2B9p4nKjGq783PgitA0M6VnjlcFclwnm5XIDCf80JBQNEKB4FxVd%2FkxIExvXr0v1bzlG9FTY4IU6j0T7qKXm7vF4vNKLC%2BonKXTwHu8sC2zjifM9mbJCVYYFIZ3BC7B9cr0r57rTeF7xWhBgtOeWyPkpwInFHoJOOMCtIIXkO5v%2BVkaOWg6mfruBHSpBN%2BRbjJlrJE88%2Bb23AU9wTIjiSn0RISi4NA1fiDshkuqKC8g9sCV4nkjYcFoqgOKl6BiM4qhRwIF%2FEzlDMa2adKwZzv12KxXl8SyrBa6pUfdhw9mljqYH1PN%2FRgf5GQMze9hWVj3swFqd1XhklNdMXqCwtIUZLp3H8e7VPB9kTTWvH39QUrfX2O5Xh45NiTj9yXhOVHiGVLqqGuNp9Uk8%2FpN7GmtHBo4W4bRrEHyvH6LzBuUnh5%2FhgxuDGc%2Fwpzt9phb5PgFTHSsNXofbR2s4L%2FULfQohJhrLRDyGrGQCnhQBU3Bhd6FLnmO5%2Bk2u5g2%2Ffk%2FmBRE8r2IySrW%2FfgwrO7aWRL9MSbdidUmsmavweNsAMda%2BwiOX2fLW3brXq820b2Dwyv2ZR1c2D0YewTKHVFxZvb9QzgOn3NO5HiL8K1D8Z8DbehAG4YvkZuSS5UCdo9sQwupcBGTDWbqBFOPnAG%2B3oRp4nVgcv8yTM73YWrZOQhTw5ueb6zj%2Bynwk2B0fTuQBwoHhBzjEscZGT5Rw2UYhdEv8A91%2FENo8rv8g%2BH5W%2Bs11vhiRdE3)" alt="Alt text" title="Optional title">

## Features

- [x] Feature 1
- [x] Feature 2
- [x] Feature 3

## Next steps
