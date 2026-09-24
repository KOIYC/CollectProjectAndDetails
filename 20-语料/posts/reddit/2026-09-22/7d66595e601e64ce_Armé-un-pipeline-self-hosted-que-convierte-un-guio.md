---
type: "corpus"
item_id: "7d66595e601e64ce"
title: "Armé un pipeline self-hosted que convierte un guion de texto en un video terminado: voz, Ken Burns, subtítulos y audio normalizado, sin editar nada a mano"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/buildinpublic/comments/1wk762t/armé_un_pipeline_selfhosted_que_convierte_un/"
author: "Easyprodigital"
published_at: "2026-09-19T08:22:15+08:00"
captured_at: "2026-09-22T12:54:39+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-22"
pub_day: "2026-09-19"
tags:
  - 语料
  - reddit
  - r/buildinpublic
metrics: {"score": 3, "comments": 2, "upvote_ratio": 0.81}
comments_count: 3
comments_total: 3
discovered_via: "reddit:7d+settle3"
---

# Armé un pipeline self-hosted que convierte un guion de texto en un video terminado: voz, Ken Burns, subtítulos y audio normalizado, sin editar nada a mano

> [!info] 一句话导读
> Me cansé de armar videos narrados a mano, así que escribí un pipeline que lo hace por mí. Ya corre de punta a punta.

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/buildinpublic/comments/1wk762t/armé_un_pipeline_selfhosted_que_convierte_un/>
> 指标：得分=3 · 评论=2 · 赞踩比=0.81
> 作者：Easyprodigital　|　发布：2026-09-19T08:22:15+08:00
> 项目链接：—
> 采集：2026-09-22T12:54:39+08:00　|　id：`7d66595e601e64ce`

## 正文

Me cansé de armar videos narrados a mano, así que escribí un pipeline que lo hace por mí. Ya corre de punta a punta.

Qué hace hoy: le paso un guion en JSON (cada escena con su texto y su imagen) y devuelve un mp4 terminado — voz generada, efecto Ken Burns, crossfades, subtítulos quemados y audio normalizado. También tiene una interfaz web para armar el guion escena por escena, y una API por si lo llamo desde n8n u otro backend.

Cómo está armado:

\- Voz con Piper (varias voces en español), espeak como respaldo, y Chatterbox si quiero clonar una voz a partir de una muestra de 10 a 30 segundos

\- El truco central: mido la duración exacta del audio generado y con eso construyo la lista de cortes. Como los tiempos salen del audio y no de detectar algo en él, el corte es determinista

\- Render con ffmpeg: Ken Burns con interpolación suave, crossfade de 0.6s, subtítulos .ass quemados

\- Audio normalizado a -16 LUFS con loudnorm (EBU R128)

\- QA automático con ffprobe antes de dar el video por bueno: duración, resolución y frames negros

\- API en FastAPI. Todo corre en mi propia máquina, cero servicios de pago

Números de la última corrida: 0.00s de diferencia entre la duración esperada y la real, 1920x1080, sin frames negros. Un video de \[X\] minutos tarda \[X\] minutos en renderizar sobre \[tu CPU\].

Lo que no funcionó:

\- Spleeter (separar voz de música) arrastra TensorFlow y se pelea con las dependencias del resto del proyecto. Terminé sacándolo a su propio servicio con su propio entorno en vez de insistir en una sola lista de dependencias

\- Para imágenes de baja resolución quedó un upscaling básico con Pillow porque todavía no conecto Real-ESRGAN. Se nota cuando el Ken Burns hace zoom sobre una imagen chica

\- Chatterbox (clonación de voz) está integrado, pero sin GPU es lentísimo al lado de Piper. Para uso ocasional sirve; para volumen

Lo que sigue es la mitad difícil: el mismo pipeline pero partiendo de audio grabado en vez de voz generada. Eso implica detectar silencios y muletillas en habla real, y ahí los tiempos dejan de ser deterministas. Todavía no lo empiezo.

Pregunta para quien haya pasado por esto: ¿qué les ha funcionado para detectar muletillas ("eh", "o sea") en español? Es la parte que más respeto me da.

## 评论（3/3）

> **No_Refrigerator1677**（1 分） · 2026-09-19T08:49:08+08:00　
> that's an impressive pipeline setup. automating that process must save so much time and effort.

---

> **QuanTradin**（1 分） · 2026-09-19T09:27:19+08:00　
> medir la duración real del audio y construir los cortes desde ahí es lo correcto, es la única parte verdaderamente determinista de todo el proceso.
>
> donde nos mordió a nosotros fue el QA automático. ffprobe te confirma duración, resolución y frames negros, y deja pasar tranquilamente un video cuyos subtítulos pertenecen a otro guion. ahora sacamos un contact sheet con tile=8x2 y lo miramos antes de dar nada por bueno.

---

> **Easyprodigital**（1 分） · 2026-09-22T04:13:57+08:00　
> https://reddit.com/link/pb8ekad/video/fufyx9n1lxqh1/player
>
> Un video de prueba crea que eata saliendo bien

## 导航

- 项目页：—（本条不是项目，按设计不建实体页）
- 渠道页：[[50-渠道/reddit]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
