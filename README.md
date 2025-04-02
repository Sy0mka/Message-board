Платформа для гильдий MMORPG с системой объявлений, откликов и email-нотификаций. Полноценный проект на Django с использованием Celery и Redis.

---

## 🌟 Основные Возможности
- **Регистрация с верификацией по Email** (с отправкой кода подтверждения)
- **Создание объявлений** с Rich-текстом (изображения/видео/форматирование)
- **Система откликов** с мгновенными email-уведомлениями
- **Приватный кабинет** с фильтрацией откликов по статусу/объявлениям
- **Рассылки** через Celery Beat (асинхронные задачи)
- **10 специализированных категорий** для гильдий (Танки, Хилы, ДД и др.)

---

## 🛠 Технологический Стек
| Компонент       | Технологии                                                                 |
|-----------------|----------------------------------------------------------------------------|
| **Backend**     | Django 4.2, Django REST Framework, Celery, Redis                           |
| **Frontend**    | Django Templates, Bootstrap 5, CKEditor                                    |
| **База данных** | PostgreSQL (оптимизированные запросы через `select_related/prefetch_related`) |
| **Инфраструктура** | Docker, Gunicorn, Nginx, .env-менеджмент                                |

---

## 🚀 Быстрый Старт
```bash
# Клонирование и запуск через Docker
git clone https://github.com/yourusername/mmorpg-board.git
cd mmorpg-board
docker-compose up --build
Настройка окружения (.env):

ini

SECRET_KEY=your-django-secret
EMAIL_HOST=smtp.yandex.ru
EMAIL_PORT=465
CELERY_BROKER=redis://redis:6379/0
POSTGRES_URL=postgres://user:pass@db:5432/mmorpg
📌 Ключевые Компоненты Кода
Модели данных (models.py)
python

class Post(models.Model):
    CATEGORIES = [
        ('tanks', 'Танки'),
        ('heals', 'Хилы'),
        ('dd', 'ДД'),
        # ... остальные категории
    ]
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=15, choices=CATEGORIES)
    title = models.CharField(max_length=255)
    content = RichTextUploadingField()  # WYSIWYG редактор
Обработка откликов (views.py)
python

class ReplyAcceptView(LoginRequiredMixin, UpdateView):
    def form_valid(self, form):
        reply = self.get_object()
        reply.status = 'accepted'
        reply.save()
        send_mail_async.delay(
            subject='Ваш отклик принят!',
            message=f'Пользователь {self.request.user} принял ваш отклик',
            recipient_list=[reply.author.email]
        )
Асинхронные задачи (tasks.py)
python

@app.task
def send_mail_async(subject, message, recipient_list):
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        recipient_list,
        fail_silently=False
    )
📈 Системные Требования
Компонент	Рекомендации
CPU	2 ядра (для Celery workers)
RAM	2GB+ (оптимально 4GB)
Хранилище	20GB+ (в зависимости от медиа-файлов)
Сеть	HTTPS с валидным сертификатом

📌 Для HR
Архитектура:

Модульное разделение apps (users, board, notifications)

Оптимизация БД через QuerySet методы

Асинхронная обработка через Celery

Безопасность:

Защита данных через .env

Масштабируемость:

Горизонтальное масштабирование Celery

Кеширование через Redis
