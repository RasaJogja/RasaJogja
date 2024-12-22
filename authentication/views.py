from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
import json
from main.models import Profile

@csrf_exempt
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            # Status login sukses.
            return JsonResponse({
                "username": user.username,
                "status": True,
                "message": "Login sukses!"
                # Tambahkan data lainnya jika ingin mengirim data ke Flutter.
            }, status=200)
        else:
            return JsonResponse({
                "status": False,
                "message": "Login gagal, akun dinonaktifkan."
            }, status=401)

    else:
        return JsonResponse({
            "status": False,
            "message": "Login gagal, periksa kembali email atau kata sandi."
        }, status=401)

@csrf_exempt
def register(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data['username']
            password1 = data['password1']
            password2 = data['password2']
            phone_number = data['phone_number']
            role = data['role']

            if password1 != password2:
                return JsonResponse({
                    "status": False,
                    "message": "Passwords do not match."
                }, status=400)

            if User.objects.filter(username=username).exists():
                return JsonResponse({
                    "status": False,
                    "message": "Username already exists."
                }, status=400)

            valid_roles = ['user', 'seller']
            if role not in valid_roles:
                return JsonResponse({
                    "status": False,
                    "message": "Invalid role selected."
                }, status=400)

            user = User.objects.create_user(username=username, password=password1)

            profile = Profile.objects.create(
                user=user,
                phone_number=phone_number,
                role=role
            )

            return JsonResponse({
                "username": user.username,
                "phone_number": profile.phone_number,
                "role": profile.role,
                "status": "success",
                "message": "User created successfully!"
            }, status=201)

        except KeyError as e:
            return JsonResponse({
                "status": False,
                "message": f"Missing required field: {str(e)}"
            }, status=400)

        except Exception as e:
            return JsonResponse({
                "status": False,
                "message": "An error occurred during registration."
            }, status=500)

    else:
        return JsonResponse({
            "status": False,
            "message": "Invalid request method."
        }, status=405)
    
@csrf_exempt
def logout(request):
    username = request.user.username

    try:
        auth_logout(request)
        return JsonResponse({
            "username": username,
            "status": True,
            "message": "Logout berhasil!"
        }, status=200)
    except:
        return JsonResponse({
        "status": False,
        "message": "Logout gagal."
        }, status=401)
