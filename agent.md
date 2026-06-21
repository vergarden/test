# Project 01 — Vue + Django 前后端分离应用

## 项目概述

Vue 3 + Vite 前端和 Django REST Framework 后端组成的全栈 Web 应用。
Django Admin 后台使用 SimpleUI 主题，默认语言为中文。

## 目录结构

```
project 01/
├── config/                 # Django 项目配置
│   ├── __init__.py
│   ├── asgi.py             # ASGI 入口
│   ├── settings.py         # 全局配置
│   ├── urls.py             # URL 路由
│   └── wsgi.py             # WSGI 入口
├── core/                   # Django 应用（主业务逻辑）
│   ├── migrations/         # 数据库迁移文件
│   ├── __init__.py
│   ├── admin.py            # 后台注册
│   ├── apps.py
│   ├── models.py           # 数据模型
│   ├── tests.py
│   └── views.py            # API 视图
├── frontend/               # Vue 3 前端
│   ├── public/             # 静态资源
│   ├── src/
│   │   ├── assets/         # 图片等资源
│   │   ├── components/     # Vue 组件
│   │   ├── App.vue         # 根组件
│   │   ├── main.js         # 入口
│   │   └── style.css       # 全局样式
│   ├── index.html          # HTML 模板
│   ├── vite.config.js      # Vite 配置
│   └── package.json
├── manage.py               # Django 管理脚本
├── db.sqlite3              # SQLite 数据库
├── static/                 # 收集的静态文件
└── venv/                   # Python 虚拟环境
```

## 技术栈

| 层       | 技术                                |
| -------- | ----------------------------------- |
| 前端     | Vue 3 + Vite                        |
| 后端     | Django 5.2 + Django REST Framework  |
| 数据库   | SQLite3（开发环境）                 |
| 后台主题 | SimpleUI                            |
| 开发语言 | Python 3.10 / JavaScript (ESM)      |

## 启动方式

### 1. 后端 (Django)

```bash
# Windows (PowerShell)
.\venv\Scripts\Activate.ps1
python manage.py runserver 0.0.0.0:8000
```

后端运行在 `http://localhost:8000/`

### 2. 前端 (Vite)

```bash
cd frontend
npm run dev
```

前端运行在 `http://localhost:5173/`

Vite 开发服务器已配置代理：
- `/api/*` → `http://127.0.0.1:8000/api/*`
- `/admin/*` → `http://127.0.0.1:8000/admin/*`
- `/static/*` → `http://127.0.0.1:8000/static/*`

开发时只需访问 `http://localhost:5173/`，API 请求会自动转发到 Django。

## 路由

### 后端 (Django)
| 路径      | 说明     |
| --------- | -------- |
| `/admin/` | 管理后台 |
| `/api/`   | API 根   |

### 前端 (Vue SPA)
| 路径 | 说明 |
| ---- | ---- |
| `/`  | 首页 |

## 管理员账号

| 字段   | 值                          |
| ------ | --------------------------- |
| 用户名 | `vergarden`                 |
| 密码   | `2008311`                   |
| 邮箱   | asdfghjkl2008311@163.com    |
| 昵称   | vergarden                   |

## 常见操作

### 创建数据库迁移
```bash
python manage.py makemigrations
python manage.py migrate
```

### 创建新应用
```bash
python manage.py startapp <app_name>
```

### 收集静态文件
```bash
python manage.py collectstatic --noinput
```

### 创建超级管理员
```bash
python manage.py createsuperuser
```

### 安装新依赖

**Python (后端):**
```bash
pip install <package>
pip freeze > requirements.txt
```

**JavaScript (前端):**
```bash
cd frontend
npm install <package>
```

## 配置要点

- **语言/时区**: `settings.py` 中 `LANGUAGE_CODE = 'zh-hans'`，`TIME_ZONE = 'Asia/Shanghai'`
- **CORS**: 仅开发环境允许 `localhost:5173` 和 `127.0.0.1:5173`
- **数据库**: 默认 SQLite3，路径为 `db.sqlite3`
- **静态文件**: `STATIC_ROOT = BASE_DIR / 'static'`
- **SimpleUI**: 替换 Django 原生后台主题，置于 `INSTALLED_APPS` 首位

## 开发注意事项

1. **编码问题**: Windows PowerShell 的 `Set-Content` 默认使用 GBK 编码。涉及中文的文件应使用 UTF-8 保存，推荐用 Python 或 VS Code 写入非 ASCII 文本。
2. **后台进程**: 使用 `Start-Process -PassThru -WindowStyle Hidden` 或 `Start-Job` 启动开发服务器。
3. **Vite HMR**: 修改前端文件后 Vite 自动热更新，通常无需手动重启。
