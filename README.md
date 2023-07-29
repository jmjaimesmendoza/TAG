# TAG Systems test project
## Project instructions
To run the lab, open a terminal on this directory then run the following command:

```
  docker compose up -d
```

Access the web application via `http://localhost:4200` on your browser.

Please wait for the backend servers to start running before testing, i'm not sure why the fastApi container in particular takes a minute or two to get going.

if you get any port already assigned errors, make sure the following ports are not busy on your machine:
- 5420
- 80
- 6379
- 8000
- 5432

## Feedback & other comments
Pretty much the only thing I would change about this test project would be to have the user store the Bearer token generated in the fastAPI either in the redis database or the browser (as cookie or in storage), why?, because this is already a more backend focused test, so actually leveraging the benefits of tokens and expiration in order to preserve the authentication info in the system would be more beneficial imo, as of right now the token is being generated and used in the same request without the option to use it more during its lifetime.  

*(I may have misunderstood this part of the test, in which case please ignore the above comment)*

---

### Little disclaimer
This is my first time using the tech stack requested minus redis/postgresql, considering this i believe i did a somewhat decent job, but the codebase for this test could most definitely be improved, particularly in the validation, testing and error handling areas.  I couldn't do anything in these two areas due to the time constraint of studiying the new frameworks and troubleshooting the dockerized lab.  I actually finished the functional requirements of the test 7/27, and spent pretty much all the remaining time learning, testing and troubleshooting the docker side of the project.

That would be all from my side, thanks for the opportunity and hope to hear back from ya'll soon!