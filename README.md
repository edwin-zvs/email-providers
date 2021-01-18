# Email Providers

This repository provides a list of email providers in csv format.

## CSV file
Check [email-providers.csv](email-providers.csv).

This list is useful when you want check if your user's email address is a
company mail address or not.

Please create a pull request to update the list.
You can add new domains at the end of the
[email-providers.csv](email-providers.csv) file and then run `python3 sort.py`
to automatically insert them at the right place.

## Rest API

This repository also provide free Rest API endpoint. The api endpoints serves up-to-dated data in the master branch.

When your pull request is merged, https://zarvis.ai will be automatically build and deploy the new version.


#### List all email providers

Request (GET)
```
https://email--providers-edwin--zvs.g1.zarvis.ai
```

Response (200, Content-Type: application/json)
```
[
    ...
    "gmail.com",
    "yahoo.com",
    ...
]
```

#### Query provider by email address or domain

Request
```
https://email--providers-edwin--zvs.g1.zarvis.ai/<email or domain>
```

Response

 - 200 - when email or domain is in the provider list
 - 404 - when email or domain is not in the provider list


Example request

```
https://email--providers-edwin--zvs.g1.zarvis.ai/foo@gmail.com
https://email--providers-edwin--zvs.g1.zarvis.ai/gmail.com
https://email--providers-edwin--zvs.g1.zarvis.ai/bar.com
```



### Thanks

Initial provider list is constructed based on
- https://gist.github.com/tbrianjones/5992856
- https://github.com/goware/emailproviders/blob/master/generate/domains.txt
- https://github.com/wesbos/burner-email-providers
