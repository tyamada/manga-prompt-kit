# サンプルPDFダウンロードページの更新

公開先：<https://tyamada.github.io/manga-prompt-kit/samples/>。

14言語の静的ページを、公開済み[PDF一覧](../releases/pdf-manifest.json)と`scripts/sample-page-locales.json`から生成します。PDF実体は固定版のGitHub Releasesに置き、`docs/`へコピーしません。JavaScriptを使わず全52冊へ到達できます。

## 更新手順

1. 新しいPDF Releaseを公開し、取得・容量・SHA-256を検証する。
2. `releases/pdf-manifest.json`の公開済み一覧を更新する。アプリ用のraw URL・schemaを維持する。
3. `python3 scripts/generate_sample_pages.py`を実行する。
4. `python3 scripts/generate_sample_pages.py --check`と`python3 scripts/validate_sample_pages.py`を実行する。
5. HTMLと一覧の差分を確認し、ルートのSHA256SUMSを更新して公開する。
6. 公開先の全言語ページとPDFリンクを確認する。

GitHub Pagesはmainブランチの`/docs`をソースとし、`.nojekyll`で静的ファイルを配信します。翻訳の修正は辞書に反映し、生成済みHTMLだけを手作業で変更しません。

## アプリからのリンク

- README.mdは`samples/en/`、README_ja.mdは`samples/ja/`へリンクする。
- 言語別Pagesは同じ言語へリンクする。zh-CN/zh_hans→zh-Hans、zh-TW/zh-HK/zh_hant→zh-Hant、tl→fil、in→id。
- 繁体字は`#zh_tw`または`#zh_hk`、スペイン語は`#es`または`#es_419`、ポルトガル語は`#pt`または`#pt_pt`で地域を指定できる。
- マレー語PDFはないため、既存msページには英語の案内へリンクする旨を明記する。Folimeldの公開Pagesは日英に対応する。
- 個別PDFの一覧表をREADME/Pagesへ再複製しない。機械処理用manifest・カタログは個別の固定PDF URLを保持する。

## PDF実体を整理するとき

各アプリの`testdata/`・`docs/`に残る漫画PDFは、アプリ・テスト・撮影・BSD等の検証スクリプトの依存を解消し、必要な配信・原本保管を確認してから削除します。一般回帰PDF、利用者が取得したPDF、同梱一覧JSONは対象外です。Git履歴の書き換えや旧2Releaseの廃止は別工程です。

2026年11月27日追加：第4話は日本語1冊のみ。既存51冊の固定URLを維持し、同一schemaの最新版JSONへep4_jaを追加しました。PDF添付の古いmanifestは当時の固定版で、現在の集約一覧はリポジトリのJSONを参照します。
