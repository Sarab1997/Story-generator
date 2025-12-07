import { useState } from "react"

export default function ThemeInput({onSubmit}){
    const [theme, setTheme]=useState("")
    const [error, setError]=useState("")

    const handleSubmit=(e)=>{
        e.preventDefault();

        if(!theme.trim()){
            setError("Please enter a theme name");
            return
        }
        
        // ADD THESE LINES:
        setError(""); // Clear any previous errors
        onSubmit(theme); // Actually call the parent's onSubmit function!
    }

    return(
       <div className="theme-input-container">
            <h2>Generate your adventure</h2>
            <p>Enter a theme for your interactive story</p>

            <form onSubmit={handleSubmit}>
                <div className="input-group">
                    <input type="text"  
                    value={theme}
                    onChange={(e)=>setTheme(e.target.value)}
                    placeholder="Enter a theme (e.g., space adventure, mystery)"
                    className={error ? 'error': ""}
                    />
                    {error && <p className="error-text">{error}</p>}
                </div>
                <button type="submit" className="generate-btn">
                    Generate Story
                </button>
            </form>
       </div>
    )
}