
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
