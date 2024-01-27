## 事前準備

1. google cloud で「Google Drive API」「Google Sheets API」を有効にする
1. 認証用の Json ファイルを生成する<br>
   API とサービル>認証>サービスアカウント>鍵の作成
1. google スプレッドシートを作成

   - 各セルに以下の文字を入力

     A1:メールアドレス、B1：件名、C1：本文

   * 2 行目以降はメール送信内容を入力
   * 共有で 2 で生成したサービスアカウントを指定

1. .env ファイルを作成\_以下の内容を記載

```
AUTH_JSON_NAME = # 2で生成したjsonファイルの名称
SHEET_URL = # スプレッドシートのURL
SMTP_HOST_NAME = # SMTPのホスト名
SMTP_PORT = # SMTPのポート番号
SMTP_USER = # SMTPのユーザー名
SMTP_PASS = # SMTPのパスワード
FROM_USER = # 送信元メールアドレス
```

## 使い方

Command memo

```
mkdir {any directory}
cd {any directory}
```

```
git clone https://github.com/hiro1321/auto_email_send_pj.git
```

```
cd auto_email_send_pj
```

- 同ディレクトリ内に事前準備の「json ファイル」「.env」を配置

```
python -m venv env
```

```
source env/bin/activate
```

```
pip install -r requirements.txt
```

```
python -m mailsendpj
```

<br>
<br>
