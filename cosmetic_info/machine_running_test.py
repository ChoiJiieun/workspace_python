from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

class CosmeticRecommender:
    def __init__(self):
        self.vectorizer = CountVectorizer()
        self.similarity_matrix = None
        self.cosmetics_df = None

    def prepare_data(self, cosmetics_data):
        """
        화장품 데이터 준비
        cosmetics_data: [
            {
                'id': 1,
                'name': '수분크림A',
                'tags': ['수분공급', '저자극', '쿨링', '피부진정'],
                'clicks': 100
            },
            ...
        ]
        """
        # 데이터프레임 생성
        self.cosmetics_df = pd.DataFrame(cosmetics_data)

        # 태그를 공백으로 구분된 문자열로 변환
        self.cosmetics_df['tags_str'] = self.cosmetics_df['tags'].apply(lambda x: ' '.join(x))

        # 태그 벡터화
        tag_vectors = self.vectorizer.fit_transform(self.cosmetics_df['tags_str'])

        # 유사도 행렬 계산
        self.similarity_matrix = cosine_similarity(tag_vectors)

    def get_similar_products(self, product_id, n_recommendations=5):
        """특정 제품과 유사한 제품 추천"""
        # 제품 인덱스 찾기
        idx = self.cosmetics_df[self.cosmetics_df['id'] == product_id].index[0]

        # 유사도 점수 계산
        similarity_scores = list(enumerate(self.similarity_matrix[idx]))

        # 유사도 기준 정렬 (자기 자신 제외)
        similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)[1:]

        # 상위 n개 추천
        top_products = []
        for i, score in similarity_scores[:n_recommendations]:
            product = self.cosmetics_df.iloc[i]
            top_products.append({
                'id': product['id'],
                'name': product['name'],
                'tags': product['tags'],
                'similarity_score': score
            })

        return top_products

# 사용 예시
sample_data = [
    {
        'id': 1,
        'name': '수분크림A',
        'tags': ['수분공급', '저자극', '쿨링', '피부진정'],
        'clicks': 150
    },
    {
        'id': 2,
        'name': '수분크림B',
        'tags': ['수분공급', '저자극', '미백', '진정'],
        'clicks': 120
    },
    {
        'id': 3,
        'name': '토너A',
        'tags': ['수분공급', '쿨링', '모공케어', '진정'],
        'clicks': 200
    }
]

# 클릭 수와 태그 유사도를 모두 고려하는 고도화된 버전
class AdvancedCosmeticRecommender(CosmeticRecommender):
    def get_weighted_recommendations(self, product_id, n_recommendations=5,
                                     click_weight=0.3, similarity_weight=0.7):
        """클릭수와 태그 유사도를 모두 고려한 추천"""
        # 기본 유사도 점수 가져오기
        idx = self.cosmetics_df[self.cosmetics_df['id'] == product_id].index[0]
        similarity_scores = list(enumerate(self.similarity_matrix[idx]))

        # 클릭수 정규화
        max_clicks = self.cosmetics_df['clicks'].max()
        normalized_clicks = self.cosmetics_df['clicks'] / max_clicks

        # 가중치를 적용한 최종 점수 계산
        weighted_scores = []
        for i, sim_score in similarity_scores:
            if i != idx:  # 자기 자신 제외
                click_score = normalized_clicks.iloc[i]
                final_score = (similarity_weight * sim_score +
                               click_weight * click_score)
                weighted_scores.append((i, final_score))

        # 최종 점수로 정렬
        weighted_scores.sort(key=lambda x: x[1], reverse=True)

        # 상위 n개 추천
        recommendations = []
        for i, score in weighted_scores[:n_recommendations]:
            product = self.cosmetics_df.iloc[i]
            recommendations.append({
                'id': product['id'],
                'name': product['name'],
                'tags': product['tags'],
                'score': score,
                'clicks': product['clicks']
            })

        return recommendations


# 사용 예시
recommender = AdvancedCosmeticRecommender()
recommender.prepare_data(sample_data)
recommendations = recommender.get_weighted_recommendations(1)

print("추천 결과:")
for rec in recommendations:
    print(f"제품명: {rec['name']}")
    print(f"태그: {', '.join(rec['tags'])}")
    print(f"점수: {rec['score']:.2f}")
    print(f"클릭수: {rec['clicks']}")
    print("---")