from rest_framework import renderers


NULLABLE = {'blank': True, 'null': True}


class MyRenderer(renderers.JSONRenderer):
    """ Класс переопределение json """
    def render(self, data, accepted_media_type=None, renderer_context=None):
        print(data)
        result = None
        # Формирование ошибки
        error = None
        if data:
            if 'Error' in str(data):
                error = data

            # Формирование результата
            elif 'results' in data:
                result = data['results']

            else:
                result = data

        # Конечный результат
        data = {"error": error, "result": result}

        return super().render(data, accepted_media_type, renderer_context)
