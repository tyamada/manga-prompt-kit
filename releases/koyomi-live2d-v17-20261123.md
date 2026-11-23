# こよみLive2Dモデル v17

『ためし部』小坂こよみの実行用モデルと編集素材です。元絵の顔立ちを使って境界を調整し、小さな左右・上下向き、傾き、まばたき、口の開閉を確認しました。

## ダウンロード

- `koyomi-live2d-v17.zip`：公開用ファイル一式。展開後は `koyomi/README.md` を参照してください。
- `SHA256SUMS`：ZIPのSHA-256。内部ファイルの照合台帳もZIP内の `verification/` に収録しています。

GitHubが自動表示するSource codeのZIP/TARはリポジトリ全体です。モデル一式だけを取得する場合は上記の添付ZIPを選んでください。

## 収録内容

- `runtime/`：MOC3、2048pxテクスチャ、モデル設定、自己紹介モーション。
- `source/`：Cubism編集用CMO3、PSD、分割PNG・境界SVG。
- `preview/`：正面画像、比較画像、音声付き確認動画と無音版動画。
- `audio/`、`docs/`、`verification/`：セリフ・調声値、再生手順、利用条件、検証・照合記録。

書き出し・確認環境：Cubism 5.3.04 FREE／SDK 5.3対応。Viewerで `runtime/koyomi.model3.json` を開き、`motions > Greeting > self-introduction` を再生します。配布モデルは無音で動きます。肩は顔の変形から分離しています。大きな横顔・毛束の物理演算は含みません。

## ライセンス：CC BY 4.0と音声の例外

**独自のモデル・編集素材・画像・モーション・文章・映像部分は、権利の存在と保有の範囲でCC BY 4.0です。** 作者・出典・ライセンスへのリンクを示し、改変した場合はその旨を明記すれば、商用利用・改変・再配布ができます。

作者：こまいろ日和（Komairo Hiyori）／校内くらし試作部

[適用範囲とクレジット例](https://github.com/tyamada/manga-prompt-kit/blob/main/live2d/koyomi/LICENSE.md) · [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.ja)

**例外：`preview/self-introduction.mp4` の合成音声はCC BY 4.0対象外です。** 音声：VOICEVOX:春日部つむぎ。音声付き動画の音声利用には[VOICEVOX規約](https://voicevox.hiroshiba.jp/term/)と[春日部つむぎ公式規約](https://tsumugi-official.studio.site/rule)が適用されます。音声部分までCC BY 4.0だけで再利用できるものではありません。

単体WAVは同梱していません。独自映像をCC BY 4.0で利用する場合は無音版 `preview/self-introduction-silent.mp4` を利用できます。自分の環境で音声を生成・追加する手順は `audio/README.md` にあります。ソフトウェア・SDK・音声ライブラリ本体は同梱しておらず、その使用には各提供元の条件が別途適用されます。
