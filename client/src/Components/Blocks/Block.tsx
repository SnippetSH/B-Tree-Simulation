export default function Block({k}: {k: number}) {
    return (
        <div className="w-10 h-10 flex justify-center items-center border-2 border-black/50 rounded-md">
            <p className="text-xl font-bold"> {k} </p>
        </div>
    )
}