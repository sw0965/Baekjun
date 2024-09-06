- 그래프 탐색의 방법 ( 탐색 알고리즘 )

   어떤것들이 연속해서 이어질때, 모두 확인하는 방법

   - Graph : Vertex(어떤 것) + Edge(이어지는 것)

   라인 : Edge 
   ㅇ : Vertex

   ㅇ    ㅇ  
   |     |
   ㅇ-ㅇ-ㅇ-ㅇ

- 그래프 탐색 종류
   - BFS : Breadth-firsh search ( 너비 우선 탐색 )
      - 자식을 우선 탐색한다
   - DFS : Depth-firsh search ( 깊이 우선 탐색 )
      - 자식 탐색 후 자식의 자식 탐색
   Queue
   input : 1, 2, 3 output : 1, 2, 3
   Stack
   input : 1, 2, 3 output : 3, 2, 1

   BFS - Queue
   DFS - Stack 

- 시간복잡도
   Big - O 표기법은 가장 최대의 시간을 뽑는 것.

   BFS : O(V+E)

- 자료구조
   
   - 검색할 그래프
   - 방문여부 확인 ( 재방문 금지 ) 
   - Queue : BFS 실행

- DFS
   - 재귀함수를 사용하기 위해 사용 -> 백트래킹
   - 재귀함수란
      - 자기 자신을 다시 호출하는 함수
      - 주의할점
         - 재귀 함수가 종료되는 시점 반드시 명시
         - 재귀함수의 깊이가 너무 깊어지면 Stack Overflow
         - DFS, 백트래킹에서 주로 사용
   - 시간복잡도
      DFS : O(V+E)