# homePy
家の中の家電をNWに繋いで動かそう！


# REST Server 
以下を叩くとローカルで動くはず

```
cd pypyServer 
python manage.py runserver
```

## Reference

* POST /api/users/
  * ユーザ追加

* GET /api/users/*
  * 指定した番号のユーザ情報を取得

* POST /api/entries/
  * デバイスの情報を追加

* GET /api/entries/*
  * 指定したデバイスの情報を取得

## Example
* http://127.0.0.1:8000/api/users/
  * body:
    ```
    {
      "name": "kani",
      "mail": "test@gmail.com"
    }
    ```

* http://127.0.0.1:8000/api/entries/
  * body:
    ```
    {
      "name": "kani-sensor",
      "sensor": "temperature",
      "body": "28.0",
      "author": 1
    }
    ```
