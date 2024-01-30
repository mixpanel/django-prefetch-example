from django.http import JsonResponse
from boards.models import Board

def all(request):
  response = {}
  
  for board in list(Board.objects.all()):
    response[board.id] = {
      "id": board.id,
      "name": board.name,
      "reports": [],
    }
    for report in board.reports.all():
      response[board.id]["reports"].append({
        "id": report.id,
        "name": report.name
      })

  return JsonResponse(response)
