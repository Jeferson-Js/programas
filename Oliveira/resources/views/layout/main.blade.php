<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>@yield('title')</title>
    @vite('resources/css/app.css')
    {{-- Google Fonts --}}
    <link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@100;400&display=swap" rel="stylesheet">
</head>
<body>    
    <header class="flex">
        <nav class="flex justify-between items-center w-full h-16 bg-red-400 shadow-md p-2">
            <h1 class="text-white">Laravel</h1>
            <ul class="flex gap-2 items-center">
                <li class="text-white"><a href="/">Home</a></li>
                <li class="text-white"><a href="/events/create">Create</a></li>
                <li class="text-white"><a href="/contact">Contact</a></li>
            </ul>
        </nav>
    </header>
        @yield('content')

    <footer class="flex justify-center items-center bg-red-400 h-16 w-full">
        <div>
            <p class="text-white">Eventos &copy; 2024</p>
        </div>
    </footer>
    <script src="https://unpkg.com/ionicons@4.5.10-0/dist/ionicons.js"></script>
</body>
</html>