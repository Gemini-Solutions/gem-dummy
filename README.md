## API Reference

#### Get

```http
  GET /test/v1/get
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `id` | `string` | **Required**. |

#### Post

```http
  Post /test/v1/post
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `employee_id`      | `string` | **Required**. Id of employee|
| `employee_name`      | `string` | **Required**. Name of employee|
| `company`      | `string` | **Required**. Company of employee|
| `experience`      | `int` | **Required**. Name of employee|

#### Put

```http
  Post /test/v1/put
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `employee_id`      | `string` | **Required**. Id of employee for which experience is updated|
| `experience`      | `int` | **Required**. Updated experience of employee |

#### Delete

```http
  Post /test/v1/delete
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `employee_id`      | `string` | **Required**. Id of employee for which data has to delete|


**Step 1**: Install gempyp in your system. Gempyp have pyprest framework under it which is used for API automation. 

**Step 2**: Create xml having Flask APIs. Features provided by pyprest are: 

            1.Key check tag is use to verify keys in responses 

            2.Post assertion is use to compare responses 

            3.Pre variables and post variables are used to define local and SUITE variables that can be used anywhere in a testcase 

            4.We can also define list of expected status codes 

            5.Pass the host URL in suite details and api tag will have endpoint
            
            6.We can also pass the env from config file as well as through cli

**Step 3**: Execute the suite.  

**Link of Suite Report**

### https://jewel.gemecosystem.com/#/autolytics/extent-report?s_run_id=GEMECO-API-PY_PROD_4C7E0037-13A1-4DBC-90D7-5735183BA2A9


