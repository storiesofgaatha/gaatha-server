from apps.work.models import Work, WorkImage, People
from collections import defaultdict
from typing import List
from asgiref.sync import sync_to_async


def work_art_work_load(keys: List[int]):
    qs = Work.objects.filter(id__in=keys)
    _map = defaultdict(list)
    for work in qs:
        _map[work.id].append(work.art_work)
    return [_map[key] for key in keys]


def work_cover_image_load(keys: List[int]):
    qs = Work.objects.filter(id__in=keys)
    _map = defaultdict(list)
    for work in qs:
        _map[work.id].append(work.cover_image)
    return [_map[key] for key in keys]


def work_image_load(keys: List[int]):
    qs = WorkImage.objects.filter(
        work__in=keys
    )
    _map = defaultdict(list)
    for workimage in qs:
        _map[workimage.work.id].append(workimage)
    return [_map[key] for key in keys]


def people_profile_picture_load(keys: List[int]):
    qs = People.objects.filter(id__in=keys)
    _map = defaultdict(list)
    for people in qs:
        _map[people.id].append(people.profile_picture)
    return [_map[key] for key in keys]


load_work_art_work = sync_to_async(work_art_work_load)
load_work_cover_image = sync_to_async(work_cover_image_load)
load_work_image = sync_to_async(work_image_load)
load_people_profile_picture = sync_to_async(people_profile_picture_load)
