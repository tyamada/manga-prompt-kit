# こよみLive2Dモデル v19（同期確認版）

v17の形状・編集素材とv18の自然な動きを継承し、Viewerの再生負荷と同期確認手順を改善しました。旧v17 Releaseは履歴として保持しています。

## ダウンロード

- `koyomi-live2d-v19.zip`：モデル・編集素材・確認動画・検証記録一式。展開後は `koyomi/README.md` を参照。
- `SHA256SUMS`：添付ZIPのSHA-256。内部ファイルの照合台帳も同梱。

GitHub自動生成のSource code ZIP/TARはリポジトリ全体です。モデルだけを取得する場合は添付ZIPを選んでください。

## 同期と再生

同一モーションと音声を使い、Viewerを1モデル描画にすると、2回の録画とも口の開始遅れは推定約26ms（測定精度約33ms）でした。動画は実機画面・システム音声を同時収録し、映像と音声を別々にずらす補正はしていません。肩の固定・顔向き・3回のまばたき・口の動きを確認しています。

Viewerでは対象モデルだけを開いて再生してください。負荷や環境により同じ精度を保証するものではありません。確認Macには既存のViewer音声開始順序修正があります。詳細は同梱の `docs/production.md` に記載しています。

配布モデルは無音で再生します。自分の環境で音声を生成・追加する手順は `audio/README.md` にあります。音声付き・無音の確認動画を両方収録しています。CMO3/PSDは形状を継承したv17のファイル名です。

## CC BY 4.0と音声の例外

独自のモデル・編集素材・画像・モーション・文章・動画の映像部分は、権利の存在と保有の範囲で **CC BY 4.0**。作者・出典・ライセンスリンクを示し、改変を明記すれば商用利用・改変・再配布ができます。

作者：こまいろ日和（Komairo Hiyori）／校内くらし試作部

[ライセンスと適用範囲](https://github.com/tyamada/manga-prompt-kit/blob/main/live2d/koyomi/LICENSE.md) · [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.ja)

**音声付き確認動画の合成音声はCC BY 4.0対象外です。** 音声：VOICEVOX:春日部つむぎ。[VOICEVOX規約](https://voicevox.hiroshiba.jp/term/)と[春日部つむぎ公式規約](https://tsumugi-official.studio.site/rule)に従ってください。無音版動画はCC BY 4.0で利用できます。

**単体WAVと個人パスが映る全画面録画は同梱していません。** ソフトウェア・SDK・音声ライブラリ本体の利用条件は各提供元のものが別途適用されます。
