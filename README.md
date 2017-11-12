# Pub/Sub Controller

## Description
GCP Pub/Subを使いやすくするためのModule。

## Usage
- Settings<br>
`setting.py`の内容を環境に合わせて編集します。<br>
    - GCP_PROJECT_ID<br>
    GCPのProjectIDを指定します。

- Pull Subscriber<br>
SubscriptionをPullする常駐プロセス。<br>
`apps/subscriber/pull/subscribe_base.py`<br>
を継承し、<br>
`received_function`をオーバーライドすると、<br>
PullSubscriptionを受け取った際に<br>
`received_function`が実行されるようになっています。
    - config<br>
    Pull Subscriberは常駐プロセスとして動作するため、<br>
    supervisorのconfigファイルを作成しています。