import System.Random
import System.Environment

data Puzzle = Puzzle { question :: String, answer :: String }

puzzles :: [Puzzle]
puzzles = [
    Puzzle "Qual è il numero che, se moltiplicato per se stesso, dà 16?" "4",
    Puzzle "Cosa si bagna mentre asciuga?" "Asciugamano",
    Puzzle "Qual è la cosa che più invecchia, più diventa piccola?" "Candela",
    Puzzle "Cos'è che ha le chiavi ma nessuna serratura, lo spazio ma nessuna stanza, puoi entrare ma non uscire?" "Tastiera",
    Puzzle "Sono stato portato al mondo per distrarmi, rubato da chi non poteva possedermi, e protetto da chi non mi ha mai visto. Cosa sono?" "Sorriso"
]

getRandomPuzzle :: IO Puzzle
getRandomPuzzle = do
    index <- randomRIO (0, length puzzles - 1)
    return $ puzzles !! index

main :: IO ()
main = do
    args <- getArgs
    case args of
        ["get"] -> do
            puzzle <- getRandomPuzzle
            putStrLn $ question puzzle
        ["check", userAnswer] -> do
            puzzle <- getRandomPuzzle
            if userAnswer == answer puzzle
                then putStrLn "Corretto!"
                else putStrLn $ "Sbagliato. La risposta corretta era: " ++ answer puzzle
        _ -> putStrLn "Uso: puzzle [get|check <risposta>]"

