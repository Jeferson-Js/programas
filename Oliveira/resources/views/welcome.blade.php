@extends('layout.main')
@section('title', 'Home')
@section('content')    

<div class="flex justify-center items-center min-h-screen">

 
    <div class="flex flex-col justify-center">
@foreach ($events as $event)
    <p>{{ $event->title }}</p>
    <p>{{ $event->Description }}</p>
    <p>{{ $event->private }}</p>
    @endforeach
</div>

</div>
@endsection