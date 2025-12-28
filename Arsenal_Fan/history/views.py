from django.shortcuts import render, get_object_or_404
from .models import Legend, Trophy, HistoryMilestone


def history_home(request):
    return milestones(request)


def milestones(request):
    milestones = HistoryMilestone.objects.all().order_by('year')
    context = {
        'milestones': milestones,
        'active_page': 'milestones'
    }
    return render(request, 'history/milestones.html', context)


def legends(request):
    legends = Legend.objects.all().order_by('order')
    context = {
        'legends': legends,
        'active_page': 'legends'
    }
    return render(request, 'history/legends.html', context)


def trophies(request):
    trophies = Trophy.objects.all()
    context = {
        'trophies': trophies,
        'active_page': 'trophies'
    }
    return render(request, 'history/trophies.html', context)


def legend_detail(request, pk):
    legend = get_object_or_404(Legend, pk=pk)
    context = {
        'legend': legend,
        'active_page': 'legends'
    }
    return render(request, 'history/legend_detail.html', context)