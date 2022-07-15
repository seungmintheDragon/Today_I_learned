# Git 기본기

- README.md
- Github 프로젝트에서 가장 먼저 보는 문서
- 일반적으로 소프트웨어 와 함께 배포
- 작성 형식은 따로 없으나, 일반적으로 마크다운을 이용해 작성



##  Repository 

**특정 디텍토리를 관리하는 **

git init   사용



REDAME.md 생성

**커밋 = 특정 버전을 남긴다**

* Working area = 내가작업하고 있는 실제 디렉토리
* Staging area = 커밋하고싶은 특정버전으로 관리하고 싶은 파일이있는곳
* Repository area = 커밋들이 저장되는곳

Working - Staging 파일이 옮겨가는것 git add

staging - Repository    git commit 실제로 저장됨

\###저장소를 만들위치에 README.md 만들기

**### vscode를 열어 터미널을 bash 로 원래잇던건 지우기**

**# git init 명령어를 통해 저장소를 버전관리**

**#git status 를 통해 내부 항목 보기**

**#git add 추적되지 않은 모든 파일과 추적하고 있는 파일 중 수정 된파일을 모두 Staging Area dp 올려요**



**# git comiit -m 'commit_message' 커밋 메세지는 자세하게**

-git config --global user.name '깃허브username'

-git config --global user.email '깃허브email'



# Git commit 실습

- 바탕화면에 edu_git_commit 폴더를 만들고 git 저장소를 생성해주세요
- 안에 a.txt. 라는 텍스트 파일을 만들고, 'add a.txt'라는 커밋메세지로 커밋을 만들어주세요
- 이번에는 b.txt 라는 텍스트파일을 만들고 'add b.txt'라는 커밋메세지로 커밋을 만들어주세요
- a.txt 파일을 수정하고  'update a.txt' 라는 커밋메세지로 커밋을 만들어주세요.



**git remote add origin '원격 저장소 url'

* git push origin master

로컬 reop 의 최신커밋을 remote repo로 푸쉬

- git clone {remote_repo}

remote_repo를 local로 복사

- git add .   :  현재 모든 파일 staging area 에 올리기
- git commit -m '커밋메세지'  : staging area 에 있는 모든파일 모두 커밋  -m 은 메세지를 남길수 있는 옵션
- git push origin master : 내가 지금까지 커밋한 내용 원격 저장소에 업데이트
- git remote add origin '깃허브 레지 url' : 어떤 원격 저장소에 깃작업을 할건지 등록

git 인증방법 : settings => developer settings => personal acess tokens 가서 토큰 발급받기



발급한토큰은 다시 볼수 없다 저장해놓기



권한설정 repo 부분만 체크 (저장소관련)

git clone '깃허브레지url' : 해당원격저장소의 파일들 현재 작업영역으로 복사



# 커밋하기전 