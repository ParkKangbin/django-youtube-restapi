from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Subscription, User # User 모델이 커스텀 User 모델이라고 가정합니다.
from .serializers import SubscriptionSerializer
from rest_framework.exceptions import ValidationError

class SubscriptionList(APIView):
    def post(self, request):
        # 요청하는 사용자(request.user)가 구독을 수행하는 주체입니다.
        subscriber = request.user
        subscribed_to_id = request.data.get('subscribed_to')

        # 기본적인 유효성 검사: 자기 자신을 구독하는 것을 방지합니다.
        if subscriber.id == subscribed_to_id:
            return Response(
                {"error": "자기 자신을 구독할 수 없습니다."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # 시리얼라이저를 위한 데이터를 준비합니다.
        # request.data를 직접 수정하는 것보다 데이터를 명시적으로 준비하는 것이 좋습니다.
        data = {
            'subscriber': subscriber.id, # 또는 subscriber.pk, 시리얼라이저에 따라 다름
            'subscribed_to': subscribed_to_id
        }

        serializer = SubscriptionSerializer(data=data)
        try:
            # 시리얼라이저의 is_valid()가 유효성 검사 실패 시 ValidationError를 발생시킵니다.
            serializer.is_valid(raise_exception=True)
            # 시리얼라이저의 save() 메서드가 모델 인스턴스를 생성합니다.
            # 만약 시리얼라이저의 create 메서드에서 subscriber 객체를 직접 기대한다면,
            # 다음과 같이 인자로 전달할 수도 있습니다: serializer.save(subscriber=subscriber)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            # ValidationError는 raise_exception=True에 의해 이미 처리됩니다.
            # 하지만 serializer.is_valid()에 의해 포착되지 않는 사용자 정의 유효성 검사 오류가 있다면,
            # 이 블록이 필요할 수 있습니다. 현재는 괜찮습니다.
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            # 예상치 못한 다른 오류를 잡습니다.
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class SubscriptionDetail(APIView):
    def delete(self, request, pk):
        # 요청하는 사용자(request.user)가 구독 취소를 수행하는 주체입니다.
        subscriber = request.user

        # 여기서 'pk'가 'subscriber'가 구독을 취소하려는 'User'의 ID라고 가정합니다.
        # 만약 'pk'가 Subscription 객체의 ID라면 쿼리는 'pk=pk'가 될 것입니다.
        # 간단한 AND 조건에는 Q 객체보다 명확한 키워드 인수를 사용하는 것이 더 읽기 좋습니다.
        subscription = get_object_or_404(
            Subscription,
            subscriber=subscriber,
            subscribed_to=pk  # pk가 구독 취소할 User의 ID라고 가정
        )
        subscription.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)