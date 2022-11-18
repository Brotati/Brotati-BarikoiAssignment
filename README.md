# Barikoi SQA Assignment

Assignment for the position of SQA Engineer.

## API Testing

In this task, I created a postman collection which contains Barikoi reverse geo API request; then I checked different places of latitude and longitude and also checked the API responses. According to the API responses I created test case documentation.

## Web Testing Automation
   In task 2, I tested "bari koi search" web page with selenium library. 
   For language I used python. After that, I created a test case 
  documentation.
## API Reference

#### Get all items

```http
  GET /api/items
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |

#### Get item

```http
  GET /api/items/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |

#### add(num1, num2)

Takes two numbers and returns the sum.

