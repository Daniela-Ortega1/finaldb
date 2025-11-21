import { useState } from "react";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Badge } from "@/components/ui/badge";
import { Calculator, TrendingUp, TrendingDown } from "lucide-react";

export default function YieldCalculator() {
  const [kgFruta, setKgFruta] = useState<string>("");
  const [kgPulpa, setKgPulpa] = useState<string>("");

  const calculateYield = () => {
    const fruta = parseFloat(kgFruta);
    const pulpa = parseFloat(kgPulpa);
    
    if (!fruta || !pulpa || fruta <= 0 || pulpa <= 0) {
      return null;
    }
    
    const rendimiento = pulpa / fruta;
    const merma = (1 - rendimiento) * 100;
    
    return {
      rendimiento: (rendimiento * 100).toFixed(2),
      merma: merma.toFixed(2)
    };
  };

  const results = calculateYield();

  return (
    <div className="min-h-screen flex items-center justify-center p-6 bg-background">
      <Card className="w-full max-w-2xl shadow-lg">
        <CardHeader className="space-y-2 text-center pb-8">
          <div className="flex items-center justify-center gap-3 mb-2">
            <div className="h-12 w-12 rounded-full bg-primary/10 flex items-center justify-center">
              <Calculator className="h-6 w-6 text-primary" />
            </div>
          </div>
          <CardTitle className="text-3xl md:text-4xl font-bold text-foreground">
            MORITA
          </CardTitle>
          <CardDescription className="text-base md:text-lg">
            Calculadora de Rendimiento de Pulpa de Mora
          </CardDescription>
        </CardHeader>

        <CardContent className="space-y-8">
          <div className="space-y-6">
            <div className="space-y-2">
              <Label htmlFor="kg-fruta" className="text-sm md:text-base font-medium">
                Kilogramos de Fruta
              </Label>
              <Input
                id="kg-fruta"
                data-testid="input-kg-fruta"
                type="number"
                step="0.01"
                min="0"
                placeholder="Ej: 100.00"
                value={kgFruta}
                onChange={(e) => setKgFruta(e.target.value)}
                className="h-12 md:h-14 text-base md:text-lg"
              />
            </div>

            <div className="space-y-2">
              <Label htmlFor="kg-pulpa" className="text-sm md:text-base font-medium">
                Kilogramos de Pulpa Obtenida
              </Label>
              <Input
                id="kg-pulpa"
                data-testid="input-kg-pulpa"
                type="number"
                step="0.01"
                min="0"
                placeholder="Ej: 65.00"
                value={kgPulpa}
                onChange={(e) => setKgPulpa(e.target.value)}
                className="h-12 md:h-14 text-base md:text-lg"
              />
            </div>
          </div>

          {results && (
            <div 
              className="grid md:grid-cols-2 gap-6 pt-4 animate-in fade-in duration-150"
              data-testid="results-display"
            >
              <Card className="p-6 bg-primary/5 border-primary/20">
                <div className="flex items-start justify-between mb-2">
                  <div className="h-10 w-10 rounded-md bg-primary/10 flex items-center justify-center">
                    <TrendingUp className="h-5 w-5 text-primary" />
                  </div>
                  <Badge variant="secondary" className="text-xs">
                    Rendimiento
                  </Badge>
                </div>
                <div className="mt-4">
                  <div className="text-2xl md:text-3xl font-bold text-foreground" data-testid="text-rendimiento">
                    {results.rendimiento}%
                  </div>
                  <p className="text-sm text-muted-foreground mt-1">
                    Eficiencia de producción
                  </p>
                </div>
              </Card>

              <Card className="p-6 bg-destructive/5 border-destructive/20">
                <div className="flex items-start justify-between mb-2">
                  <div className="h-10 w-10 rounded-md bg-destructive/10 flex items-center justify-center">
                    <TrendingDown className="h-5 w-5 text-destructive" />
                  </div>
                  <Badge variant="secondary" className="text-xs">
                    Pérdida
                  </Badge>
                </div>
                <div className="mt-4">
                  <div className="text-2xl md:text-3xl font-bold text-foreground" data-testid="text-merma">
                    {results.merma}%
                  </div>
                  <p className="text-sm text-muted-foreground mt-1">
                    Porcentaje de merma
                  </p>
                </div>
              </Card>
            </div>
          )}

          {!results && kgFruta && kgPulpa && (
            <div className="text-center text-sm text-muted-foreground p-4 bg-muted/50 rounded-md">
              Ingrese valores válidos mayores a 0 para calcular
            </div>
          )}
        </CardContent>

        <div className="px-6 pb-6 text-center">
          <p className="text-sm text-muted-foreground">
            Proyecto MORITA - Control de Calidad y Eficiencia
          </p>
        </div>
      </Card>
    </div>
  );
}
