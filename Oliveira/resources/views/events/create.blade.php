@extends('layout.main')
@section('title', 'Create')
@section('content')    
<div class="flex justify-center items-center min-h-screen">

    <form action="/events" method="POST">
        @csrf
        <div class="flex flex-col justify-center items-center">
            <h1>Create</h1>
            <input type="text" name="title" placeholder="Crie um titulo" class="w-64 p-2 shadow-md border-none mb-3">
            <input type="text" name="city" placeholder="Sua cidade" class="w-64 p-2 shadow-md border-none mb-3">
            <label for="description" class="mb-3">O evento é privado ?</label>
            <select name="private" id="private" class="p-2 shadow-md border-none mb-3 w-28">
                <option value="0" class="bg-red-300 text-white">Não</option>
                <option value="1" class="bg-green-300 text-white">Sim</option>
            </select>
            <label for="description">Descrição do evento</label>
            <textarea name="description" id="description" cols="30" rows="5" placeholder="Descrição do evento" class="mb-3 p-2"></textarea>
            <input type="submit" value="Create" class=" cursor-pointer p-1 bg-green-500 hover:bg-green-400 duration-500 text-white rounded shadow-md w-20">
        </div>
    </form>
    
</div>
@endsection
