from strawberry.django.views import AsyncGraphQLView
from starlette.requests import Request
from starlette.responses import Response
from typing import Any, Optional
from strawberry.dataloader import DataLoader

from apps.work.dataloaders import (
    load_work_art_work,
    load_work_image,
    load_work_cover_image,
    load_people_profile_picture
)


class CustomAsyncGraphQLView(AsyncGraphQLView):
    async def get_context(self, request: Request, response: Optional[Response]) -> Any:
        return {
            'request': request,
            'work_art_work_loader': DataLoader(load_fn=load_work_art_work),
            'work_cover_image_loader': DataLoader(load_fn=load_work_cover_image),
            'work_image_loader': DataLoader(load_fn=load_work_image),
            'people_profile_picture_loader': DataLoader(load_fn=load_people_profile_picture),
        }
