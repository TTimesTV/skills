# 리서치 노트

확인일: 2026-10-08. 공식 문서와 제작자 공개 글의 텍스트를 검토했다. 임베드된 튜토리얼 영상의 전체 재생이나 직접 모델 비교 실험은 하지 않았다. 아래 요약은 성공률 검증이 아니다.

## 공식 가이드

1. [Runway Gen-4 Video Prompting Guide](https://help.runwayml.com/hc/en-us/articles/39789879462419-Gen-4-Video-Prompting-Guide)
   - 입력 이미지가 구도·외형을 담당하고 글은 움직임에 집중하도록 권장한다. 기본 동작부터 한 요소씩 추가하고 긍정문을 사용한다.
   - 적용: 잘못된 시점 이미지를 긴 문장으로 억지 교정하지 않는다. 부정문 비권장 범위는 이 모델 가이드에 한정한다.
2. [Runway Image to Video Prompting Guide](https://help.runwayml.com/hc/en-us/articles/48324313115155-Image-to-Video-Prompting-Guide)
   - 시작 이미지의 시각적 단서가 이동 지시와 충돌할 수 있다. 순서나 대략적인 타이밍을 서술할 수 있고, 마지막 프레임을 다음 생성에 사용할 수 있다.
   - 적용: 같은 실패가 반복되면 입력 이미지도 점검한다. 프레임 연결 후에는 속도와 접합을 따로 확인한다.
3. [Google DeepMind Veo Prompt Guide](https://deepmind.google/models/veo/prompt-guide/)
   - 구도, 카메라 움직임, 조명, 장면과 행동을 구체화하며 짧거나 긴 프롬프트 모두 예시로 다룬다.
   - 적용: 무조건 짧게 쓰기보다 모델과 샷 복잡도에 맞춘다. 상세 타이밍을 정확한 실행 보장으로 설명하지 않는다.
4. [ElevenLabs Image & Video capabilities](https://elevenlabs.io/docs/overview/capabilities/image-video)
   - 모델별 입력이 다르다. 확인 당시 Seedance 1 Pro는 시작/끝 프레임을, LTX 2 Retake는 원본 영상과 텍스트를 설명한다. Retake의 이미지 조건 지원은 이 설명에서 확인되지 않았다.
   - 적용: ElevenLabs라는 서비스명만으로 이미지 편집이나 끝 프레임 지원을 단정하지 않는다. 현재 UI·모델·모드와 호환 조합을 재확인한다.
5. [Adobe: Match camera motion](https://helpx.adobe.com/ie/firefly/web/work-with-audio-and-video/work-with-video/match-camera-motion-to-reference-video.html) / [Adobe: Video Editor generation](https://helpx.adobe.com/firefly/web/firefly-video-editor/generate-videos/generate-video-using-firefly-models.html)
   - 첫 문서는 모션 참고 영상과 프레임 옵션을 안내하지만 Video Editor 문서는 시작/끝 프레임을 넣으면 모션/구도 참고 등 일부 옵션이 비활성화된다고 안내한다.
   - 적용: 서로 다른 화면의 기능 설명을 합쳐 존재하지 않는 워크플로를 만들지 않는다. 사용 중인 화면에서 조합을 확인한다.

## 제작자·사용자 경험

6. [Premiere Gal / Kelsey Brannan: Borrow camera motion, Adobe tutorial](https://helpx.adobe.com/ca/firefly/how-to/video-motion-reference.html)
   - 제작자 튜토리얼의 공개 텍스트는 직접 촬영한 pan/zoom/circle 동작을 모션 참고로 쓰는 접근을 제시한다.
   - 채택: 공간 외형과 카메라 움직임의 참고 자료를 분리한다. 사용 모델에 모션 참조 입력이 있을 때 적용한다. 튜토리얼 영상 자체는 미검증.
7. [FXI Studio: Frame-chain AI video](https://www.fxi.studio/tutorials/frame-chain-ai-video-first-frame-last-frame)
   - 창업자 Alverson Layne의 제작 워크플로는 이전 샷 마지막 프레임을 다음 샷 시작에 연결하고 편집에서 속도를 다듬는다. 상업 스튜디오의 공개 경험이다.
   - 채택: 프레임을 연결 기준으로 사용. 공유 프레임만으로 완벽한 연결이 보장된다는 홍보성 표현은 채택하지 않는다.
8. [Reddit r/runwayml: Camera movement](https://www.reddit.com/r/runwayml/comments/1luwaz6/camera_movement/)
   - 이용자들이 orbit 지시의 어려움을 보고하고 각도·방향 명시 등의 제안을 나눈다. 일부 제안은 작성자도 해당 모델에서 시험하지 않았다고 밝힌다.
   - 적용: 실패 유형의 참고만 한다. 각도 문구를 검증된 해결법이나 공식 노하우로 소개하지 않는다. 계정명만으로 직원이라고 추정하지 않는다.

## 이 스킬이 별도로 정한 실무 규칙

다음은 위 자료와 사용자 사례를 종합한 설계 제안이며 공식 보장이 아니다: 상세 연출 설계와 모델 실행문 분리, 동일 공간 오류 두 번 후 입력/모드 재검토, 이동·시선·건물 방향 분리, 원본 앞부분은 편집에서 보존, 끝 프레임의 지리 검증 후 생성. 프롬프트만으로 실제 도시의 정확한 3D 복원을 보장하지 않는다.
