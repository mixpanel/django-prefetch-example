from django.http import JsonResponse
from boards.models import Board
from django.db.models import Prefetch

def all(request):
  response = {}
  boards = Board.objects.all()

  for board in list(boards):
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

def all_prefetch(request):
  response = {}
  # Look at this "prefetch_related" stuff, that's all!
  boards = Board.objects.prefetch_related(Prefetch('reports', to_attr='reports_list'))

  for board in list(boards):
    response[board.id] = {
      "id": board.id,
      "name": board.name,
      "reports": [],
    }
    for report in board.reports_list:
      response[board.id]["reports"].append({
        "id": report.id,
        "name": report.name
      })

  return JsonResponse(response)

def first(request):
  board = Board.objects.first()
  response = {
    "id": board.id,
    "name": board.name,
    "reports": [],
  }
  for report in board.reports.all():
    response["reports"].append({
      "id": report.id,
      "name": report.name
    })

  return JsonResponse(response)

def last(request):
  board = Board.objects.last()
  response = {
    "id": board.id,
    "name": board.name,
    "reports": [],
  }
  for report in board.reports.all():
    response["reports"].append({
      "id": report.id,
      "name": report.name
    })

  return JsonResponse(response)