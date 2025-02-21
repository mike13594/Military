from django.shortcuts import render, redirect
from users.forms import LoginForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def profile(request):
    return render(request, "profile.html")

def login_view(request):
    # print(request)
    # print(request.user)

    # 로그인 user 유효성 검증하는 부분
    if request.user.is_authenticated:
        return redirect("/post/")
    
    # LoginForm 에서 로그인 버튼을 누르면 처리하는 부분 
    if request.method == "POST":
        form = LoginForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            # username, password에 해당하는 사용자가 있는지 검사
            # 해당 정보가 있는지 여부 확인, 정보가 없으면 None 반환
            user = authenticate(username=username, password=password)

            # 해당 사용자가 존재하면
            if user:
                # 로그인 처리 후, 게시글 첫 화면으로 redirect
                login(request, user)
                return redirect("/post/")
            
            # 사용자가 없다면 form에서 에러 추가
            else:
                form.add_error(None, "입력한 자격증명에 해당하는 사용자가 없습니다.")

        # 어떤 경우든지 실패한 경우 다시 LoginForm을 사용한 로그인 페이지 렌더링
        context = {"form" : form}
        return render(request, "login.html", context)    

    else:
        # LoginForm 빈 인스턴스를 생성
        form = LoginForm()

        context = {
            "form" : form
        }

        return render(request, "login.html", context)        
    
