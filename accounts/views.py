from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    """new_user登録"""
    if request.method != 'POST':
        # 空のUser登録Formを表示
        form = UserCreationForm()
    else:
        # 入力済みのFormを処理
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # UserをログインさせHomePageにredirect
            login(request, new_user)
            return redirect('learning_logs:index')
        
    # 空または無効のFormを表示
    context = {'form': form}
    return render(request, 'registration/register.html', context)
