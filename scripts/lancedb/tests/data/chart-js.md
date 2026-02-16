# chartjs-plugin-datalabels

chartjs-plugin-datalabels is a highly customizable Chart.js plugin that displays labels directly on data elements for any chart type. It enables developers to add visual annotations showing data values, custom text, or formatted information on bars, lines, points, arcs, and other chart elements. The plugin integrates seamlessly with Chart.js 3.x and 4.x, providing extensive styling options including colors, fonts, backgrounds, borders, and positioning.

The plugin supports advanced features like scriptable options for dynamic label generation, multiple labels per data point, event listeners for interactive behaviors, and automatic overlap detection. It offers precise control over label positioning through anchor points, alignment presets, rotation, and offset values. Labels can be configured globally, per-chart, or per-dataset, enabling flexible customization patterns that scale from simple value displays to complex multi-label visualizations with conditional formatting.

## Installation and Registration

### npm Installation

```bash
npm install chartjs-plugin-datalabels --save
```

### Global Registration

```javascript
import { Chart } from 'chart.js';
import ChartDataLabels from 'chartjs-plugin-datalabels';

// Register plugin globally for all charts
Chart.register(ChartDataLabels);

// Create chart - plugin is automatically active
const chart = new Chart(ctx, {
  type: 'bar',
  data: {
    labels: ['Q1', 'Q2', 'Q3', 'Q4'],
    datasets: [{
      label: 'Revenue',
      data: [45, 67, 52, 89]
    }]
  }
});
```

### Per-Chart Registration

```javascript
import { Chart } from 'chart.js';
import ChartDataLabels from 'chartjs-plugin-datalabels';

// Register plugin only for specific chart instance
const chart = new Chart(ctx, {
  type: 'line',
  plugins: [ChartDataLabels],
  data: {
    labels: ['Jan', 'Feb', 'Mar', 'Apr'],
    datasets: [{
      label: 'Sales',
      data: [12, 19, 8, 15]
    }]
  },
  options: {
    plugins: {
      datalabels: {
        color: '#36A2EB'
      }
    }
  }
});
```

### CDN Usage

```html
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.0.0/dist/chart.umd.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/chartjs-plugin-datalabels@2.2.0"></script>

<canvas id="myChart"></canvas>

<script>
  // Plugin available as global ChartDataLabels
  Chart.register(ChartDataLabels);

  const ctx = document.getElementById('myChart');
  const chart = new Chart(ctx, {
    type: 'doughnut',
    data: {
      labels: ['Red', 'Blue', 'Yellow'],
      datasets: [{
        data: [300, 50, 100],
        backgroundColor: ['#FF6384', '#36A2EB', '#FFCE56']
      }]
    },
    options: {
      plugins: {
        datalabels: {
          color: 'white',
          font: {
            weight: 'bold',
            size: 16
          }
        }
      }
    }
  });
</script>
```

## Configuration Levels

### Three-Level Configuration Hierarchy

```javascript
import { Chart } from 'chart.js';
import ChartDataLabels from 'chartjs-plugin-datalabels';

Chart.register(ChartDataLabels);

// Level 1: Global defaults for all charts
Chart.defaults.set('plugins.datalabels', {
  color: '#FE777B',
  font: {
    weight: 'bold'
  }
});

// Level 2: Chart-specific options
const chart = new Chart(ctx, {
  type: 'bar',
  data: {
    labels: ['A', 'B', 'C', 'D'],
    datasets: [
      {
        label: 'Dataset 1',
        data: [10, 20, 30, 40],
        backgroundColor: '#36A2EB',
        // Level 3: Dataset-specific options (highest priority)
        datalabels: {
          color: '#FFCE56',
          anchor: 'end',
          align: 'top'
        }
      },
      {
        label: 'Dataset 2',
        data: [15, 25, 35, 45],
        backgroundColor: '#FF6384',
        datalabels: {
          color: 'white',
          anchor: 'center'
        }
      }
    ]
  },
  options: {
    plugins: {
      // Level 2: All labels in this chart
      datalabels: {
        backgroundColor: 'rgba(0, 0, 0, 0.7)',
        borderRadius: 4,
        padding: 6
      }
    }
  }
});
```

## Formatter Function

### Custom Data Formatting

```javascript
const chart = new Chart(ctx, {
  type: 'bar',
  data: {
    labels: ['Product A', 'Product B', 'Product C'],
    datasets: [{
      label: 'Sales',
      data: [0.234, 0.456, 0.789]
    }]
  },
  options: {
    plugins: {
      datalabels: {
        formatter: function(value, context) {
          // Convert decimal to percentage
          return Math.round(value * 100) + '%';
        }
      }
    }
  }
});
// Labels display: "23%", "46%", "79%"
```

### Using Built-in Functions

```javascript
const chart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: ['Week 1', 'Week 2', 'Week 3'],
    datasets: [{
      data: [12.7, 45.3, 23.8]
    }]
  },
  options: {
    plugins: {
      datalabels: {
        formatter: Math.round
        // Labels display: "13", "45", "24"
      }
    }
  }
});
```

### Context-Based Formatting

```javascript
const chart = new Chart(ctx, {
  type: 'doughnut',
  data: {
    labels: ['Alpha', 'Beta', 'Gamma', 'Delta'],
    datasets: [{
      data: [42, 24, 18, 16]
    }]
  },
  options: {
    plugins: {
      datalabels: {
        formatter: function(value, context) {
          // Access chart labels and data index
          const label = context.chart.data.labels[context.dataIndex];
          const datasetLabel = context.dataset.label || '';
          const percentage = ((value / 100) * 100).toFixed(1);

          return label + '\n' + percentage + '%';
        },
        textAlign: 'center',
        font: {
          lineHeight: 1.5
        }
      }
    }
  }
});
// Labels display multiline: "Alpha\n42.0%", "Beta\n24.0%", etc.
```

### Conditional Formatting

```javascript
const chart = new Chart(ctx, {
  type: 'bar',
  data: {
    labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
    datasets: [{
      label: 'Performance',
      data: [85, 92, 78, 95, 88]
    }]
  },
  options: {
    plugins: {
      datalabels: {
        formatter: function(value, context) {
          // Add emoji indicators based on value
          if (value >= 90) return '🟢 ' + value;
          if (value >= 80) return '🟡 ' + value;
          return '🔴 ' + value;
        },
        color: function(context) {
          const value = context.dataset.data[context.dataIndex];
          return value >= 90 ? '#22C55E' : value >= 80 ? '#EAB308' : '#EF4444';
        }
      }
    }
  }
});
```

## Positioning and Alignment

### Anchor and Align Presets

```javascript
const chart = new Chart(ctx, {
  type: 'bar',
  data: {
    labels: ['Start', 'Center', 'End'],
    datasets: [{
      label: 'Positive Values',
      data: [50, 75, 100],
      datalabels: {
        anchor: 'end',      // Position at highest element boundary
        align: 'top',       // Place label above anchor point
        offset: 4           // 4px spacing from anchor
      }
    }, {
      label: 'Negative Values',
      data: [-30, -45, -60],
      datalabels: {
        anchor: 'end',      // Position at lowest element boundary
        align: 'bottom',    // Place label below anchor point
        offset: 4
      }
    }]
  },
  options: {
    plugins: {
      datalabels: {
        backgroundColor: 'rgba(0, 0, 0, 0.8)',
        color: 'white',
        borderRadius: 3,
        padding: 4,
        font: {
          weight: 'bold'
        }
      }
    }
  }
});
```

### Angular Alignment

```javascript
const chart = new Chart(ctx, {
  type: 'polarArea',
  data: {
    labels: ['North', 'East', 'South', 'West'],
    datasets: [{
      data: [11, 16, 7, 13],
      backgroundColor: ['#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0']
    }]
  },
  options: {
    plugins: {
      datalabels: {
        anchor: 'end',
        align: function(context) {
          // Calculate angle in degrees
          const dataIndex = context.dataIndex;
          const total = context.chart.data.labels.length;
          return (360 / total) * dataIndex;
        },
        offset: 12,
        color: 'white',
        font: {
          size: 14,
          weight: 'bold'
        }
      }
    }
  }
});
```

### Rotation

```javascript
const chart = new Chart(ctx, {
  type: 'bar',
  data: {
    labels: ['Very Long Label A', 'Very Long Label B', 'Very Long Label C'],
    datasets: [{
      data: [45, 67, 52]
    }]
  },
  options: {
    indexAxis: 'x',
    plugins: {
      datalabels: {
        anchor: 'end',
        align: 'start',
        rotation: -45,      // Rotate 45 degrees counter-clockwise
        offset: 8,
        font: {
          size: 12
        }
      }
    }
  }
});
```

### Clamping for Overflow

```javascript
const chart = new Chart(ctx, {
  type: 'bar',
  data: {
    labels: ['A', 'B', 'C', 'D'],
    datasets: [{
      data: [120, 95, 150, 80]
    }]
  },
  options: {
    scales: {
      y: {
        max: 100  // Values exceed scale maximum
      }
    },
    plugins: {
      datalabels: {
        anchor: 'end',
        align: 'end',
        clamp: true,  // Constrain anchor to visible element geometry
        color: '#DC2626',
        font: {
          weight: 'bold'
        }
      }
    }
  }
});
```

## Styling Options

### Colors and Fonts

```javascript
const chart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
    datasets: [{
      label: 'Revenue',
      data: [1200, 1900, 1500, 2100, 1800],
      borderColor: '#8B5CF6',
      backgroundColor: 'rgba(139, 92, 246, 0.1)'
    }]
  },
  options: {
    plugins: {
      datalabels: {
        color: '#8B5CF6',
        font: {
          family: 'Arial',
          size: 14,
          weight: 'bold',
          style: 'italic',
          lineHeight: 1.2
        },
        textAlign: 'center'
      }
    }
  }
});
```

### Background and Borders

```javascript
const chart = new Chart(ctx, {
  type: 'doughnut',
  data: {
    labels: ['Development', 'Design', 'Marketing'],
    datasets: [{
      data: [45, 30, 25],
      backgroundColor: ['#3B82F6', '#10B981', '#F59E0B']
    }]
  },
  options: {
    plugins: {
      datalabels: {
        color: 'white',
        backgroundColor: 'rgba(0, 0, 0, 0.9)',
        borderColor: 'white',
        borderWidth: 2,
        borderRadius: 8,
        padding: {
          top: 8,
          right: 12,
          bottom: 8,
          left: 12
        },
        font: {
          size: 16,
          weight: 'bold'
        }
      }
    }
  }
});
```

### Text Shadow and Stroke

```javascript
const chart = new Chart(ctx, {
  type: 'radar',
  data: {
    labels: ['Speed', 'Power', 'Defense', 'Agility', 'Stamina'],
    datasets: [{
      label: 'Character Stats',
      data: [8, 7, 9, 6, 8],
      backgroundColor: 'rgba(255, 99, 132, 0.2)',
      borderColor: 'rgb(255, 99, 132)'
    }]
  },
  options: {
    plugins: {
      datalabels: {
        color: 'white',
        textStrokeColor: '#000000',
        textStrokeWidth: 3,
        textShadowBlur: 10,
        textShadowColor: 'rgba(0, 0, 0, 0.8)',
        font: {
          size: 18,
          weight: 'bold'
        }
      }
    }
  }
});
```

### Opacity and Display Control

```javascript
const chart = new Chart(ctx, {
  type: 'bubble',
  data: {
    datasets: [{
      label: 'Dataset 1',
      data: [
        { x: 20, y: 30, r: 15 },
        { x: 40, y: 10, r: 10 },
        { x: 60, y: 45, r: 25 },
        { x: 80, y: 20, r: 8 }
      ],
      backgroundColor: '#36A2EB'
    }]
  },
  options: {
    plugins: {
      datalabels: {
        display: function(context) {
          // Only show labels for bubbles with radius > 10
          return context.dataset.data[context.dataIndex].r > 10;
        },
        opacity: function(context) {
          // Vary opacity based on bubble size
          const radius = context.dataset.data[context.dataIndex].r;
          return radius / 25;  // Larger bubbles = more opaque labels
        },
        formatter: function(value) {
          return 'R=' + value.r;
        },
        color: 'white',
        font: {
          weight: 'bold'
        }
      }
    }
  }
});
```

## Scriptable Options

### Dynamic Label Styling

```javascript
const chart = new Chart(ctx, {
  type: 'bar',
  data: {
    labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    datasets: [{
      label: 'Monthly Sales',
      data: [65, 59, 80, 81, 56, 95],
      backgroundColor: '#3B82F6'
    }]
  },
  options: {
    plugins: {
      datalabels: {
        color: function(context) {
          const value = context.dataset.data[context.dataIndex];
          // Red for below 60, yellow for 60-80, green for above 80
          return value < 60 ? '#EF4444' : value < 80 ? '#F59E0B' : '#10B981';
        },
        backgroundColor: function(context) {
          return context.active ? 'rgba(0, 0, 0, 0.9)' : 'rgba(0, 0, 0, 0.7)';
        },
        font: function(context) {
          const value = context.dataset.data[context.dataIndex];
          return {
            weight: value > 80 ? 'bold' : 'normal',
            size: context.active ? 16 : 12
          };
        },
        formatter: function(value, context) {
          const prefix = context.datasetIndex === 0 ? '$' : '';
          return prefix + value + 'K';
        },
        padding: 6,
        borderRadius: 4
      }
    }
  }
});
```

### Index and Dataset Based Styling

```javascript
const chart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: ['Q1', 'Q2', 'Q3', 'Q4'],
    datasets: [
      {
        label: '2023',
        data: [100, 120, 115, 134],
        borderColor: '#3B82F6'
      },
      {
        label: '2024',
        data: [110, 135, 128, 152],
        borderColor: '#10B981'
      }
    ]
  },
  options: {
    plugins: {
      datalabels: {
        display: function(context) {
          // Only show labels for last data point of each dataset
          return context.dataIndex === context.chart.data.labels.length - 1;
        },
        color: function(context) {
          // Match label color to line color
          return context.dataset.borderColor;
        },
        backgroundColor: 'white',
        borderColor: function(context) {
          return context.dataset.borderColor;
        },
        borderWidth: 2,
        borderRadius: 4,
        padding: 6,
        font: {
          weight: 'bold',
          size: 14
        },
        formatter: function(value, context) {
          return context.dataset.label + ': ' + value;
        }
      }
    }
  }
});
```

## Multiple Labels

### Multi-Label Configuration

```javascript
const chart = new Chart(ctx, {
  type: 'doughnut',
  data: {
    labels: ['Earth', 'Mars', 'Saturn', 'Jupiter'],
    datasets: [{
      data: [45, 25, 60, 82],
      backgroundColor: ['#3B82F6', '#EF4444', '#F59E0B', '#10B981']
    }]
  },
  options: {
    plugins: {
      datalabels: {
        labels: {
          // First label: shows index number
          index: {
            align: 'end',
            anchor: 'end',
            color: function(context) {
              return context.dataset.backgroundColor[context.dataIndex];
            },
            font: { size: 18, weight: 'bold' },
            formatter: function(value, context) {
              return '#' + (context.dataIndex + 1);
            },
            offset: 8,
            opacity: 0.8
          },
          // Second label: shows planet name
          name: {
            align: 'top',
            anchor: 'center',
            color: 'white',
            font: { size: 16, weight: 'bold' },
            formatter: function(value, context) {
              return context.chart.data.labels[context.dataIndex];
            }
          },
          // Third label: shows value with styling
          value: {
            align: 'bottom',
            anchor: 'center',
            backgroundColor: function(context) {
              const value = context.dataset.data[context.dataIndex];
              return value > 50 ? 'white' : null;
            },
            borderColor: 'white',
            borderWidth: 2,
            borderRadius: 4,
            color: function(context) {
              const value = context.dataset.data[context.dataIndex];
              return value > 50 ? context.dataset.backgroundColor[context.dataIndex] : 'white';
            },
            formatter: function(value) {
              return Math.round(value);
            },
            padding: 4,
            font: { size: 14 }
          }
        }
      }
    }
  }
});
```

### Conditional Multiple Labels

```javascript
const chart = new Chart(ctx, {
  type: 'bar',
  data: {
    labels: ['Product A', 'Product B', 'Product C', 'Product D'],
    datasets: [{
      label: 'Revenue',
      data: [12500, 18750, 9200, 21300]
    }]
  },
  options: {
    plugins: {
      datalabels: {
        labels: {
          title: {
            anchor: 'end',
            align: 'top',
            color: '#1F2937',
            font: { weight: 'bold', size: 14 },
            formatter: function(value, context) {
              return context.chart.data.labels[context.dataIndex];
            }
          },
          value: {
            anchor: 'end',
            align: 'bottom',
            backgroundColor: 'rgba(0, 0, 0, 0.8)',
            color: 'white',
            borderRadius: 4,
            padding: 4,
            font: { size: 12 },
            formatter: function(value) {
              return '$' + (value / 1000).toFixed(1) + 'K';
            },
            offset: -4,
            display: function(context) {
              // Only show value label if revenue > 10000
              return context.dataset.data[context.dataIndex] > 10000;
            }
          }
        }
      }
    }
  }
});
```

## Event Listeners

### Click Event Handling

```javascript
const chart = new Chart(ctx, {
  type: 'pie',
  data: {
    labels: ['Option A', 'Option B', 'Option C', 'Option D'],
    datasets: [{
      data: [30, 45, 15, 10],
      backgroundColor: ['#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0']
    }]
  },
  options: {
    plugins: {
      datalabels: {
        color: 'white',
        font: { weight: 'bold', size: 14 },
        listeners: {
          click: function(context, event) {
            // Handle label click
            const dataIndex = context.dataIndex;
            const value = context.dataset.data[dataIndex];
            const label = context.chart.data.labels[dataIndex];

            console.log('Clicked:', label, 'with value:', value);
            console.log('Mouse position:', event.x, 'x', event.y);
            console.log('Native event:', event.native);

            // Check for modifier keys
            if (event.native.ctrlKey) {
              alert('Ctrl+Click detected on ' + label);
            }

            // Return false to prevent chart update
            return false;
          }
        }
      }
    }
  }
});
```

### Hover Interactions

```javascript
const chart = new Chart(ctx, {
  type: 'bar',
  data: {
    labels: ['Item 1', 'Item 2', 'Item 3', 'Item 4'],
    datasets: [{
      label: 'Sales',
      data: [45, 67, 52, 89],
      backgroundColor: '#3B82F6'
    }]
  },
  options: {
    plugins: {
      datalabels: {
        listeners: {
          enter: function(context, event) {
            // Mouse enters label area
            context.hovered = true;
            console.log('Entered label at index:', context.dataIndex);

            // Return true to trigger label update and chart re-render
            return true;
          },
          leave: function(context, event) {
            // Mouse leaves label area
            context.hovered = false;
            console.log('Left label at index:', context.dataIndex);

            // Return true to trigger label update and chart re-render
            return true;
          }
        },
        // Use custom context property in scriptable options
        color: function(context) {
          return context.hovered ? '#DC2626' : '#1F2937';
        },
        backgroundColor: function(context) {
          return context.hovered ? '#FEF3C7' : 'rgba(0, 0, 0, 0.1)';
        },
        font: function(context) {
          return {
            weight: context.hovered ? 'bold' : 'normal',
            size: context.hovered ? 16 : 12
          };
        },
        padding: 6,
        borderRadius: 4
      }
    }
  }
});
```

### Dataset-Specific Event Listeners

```javascript
const chart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: ['Week 1', 'Week 2', 'Week 3', 'Week 4'],
    datasets: [
      {
        label: 'Store A',
        data: [12, 19, 15, 22],
        borderColor: '#3B82F6',
        datalabels: {
          listeners: {
            click: function(context, event) {
              alert('Store A - Week ' + (context.dataIndex + 1) + ': ' +
                    context.dataset.data[context.dataIndex] + ' sales');
              return false;
            }
          }
        }
      },
      {
        label: 'Store B',
        data: [8, 14, 11, 18],
        borderColor: '#10B981',
        datalabels: {
          listeners: {
            click: function(context, event) {
              alert('Store B - Week ' + (context.dataIndex + 1) + ': ' +
                    context.dataset.data[context.dataIndex] + ' sales');
              return false;
            }
          }
        }
      }
    ]
  },
  options: {
    plugins: {
      datalabels: {
        backgroundColor: 'rgba(0, 0, 0, 0.8)',
        color: 'white',
        borderRadius: 4,
        padding: 4,
        font: { size: 12 }
      }
    }
  }
});
```

## Display Control and Clipping

### Auto Display with Overlap Detection

```javascript
const chart = new Chart(ctx, {
  type: 'scatter',
  data: {
    datasets: [{
      label: 'Data Points',
      data: [
        { x: 10, y: 20 },
        { x: 15, y: 25 },  // Close to previous point
        { x: 12, y: 22 },  // Overlapping area
        { x: 50, y: 30 },
        { x: 80, y: 60 }
      ],
      backgroundColor: '#FF6384'
    }]
  },
  options: {
    plugins: {
      datalabels: {
        display: 'auto',  // Automatically hide overlapping labels
        formatter: function(value, context) {
          return 'Point ' + (context.dataIndex + 1);
        },
        backgroundColor: 'rgba(0, 0, 0, 0.8)',
        color: 'white',
        borderRadius: 4,
        padding: 6,
        font: { size: 11 }
      }
    }
  }
});
// Labels at indices 1 and 2 may be automatically hidden if they overlap
```

### Conditional Display Logic

```javascript
const chart = new Chart(ctx, {
  type: 'bar',
  data: {
    labels: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
    datasets: [{
      data: [5, 45, 12, 78, 3, 89, 34, 67]
    }]
  },
  options: {
    plugins: {
      datalabels: {
        display: function(context) {
          const value = context.dataset.data[context.dataIndex];
          const dataIndex = context.dataIndex;

          // Show labels only for:
          // 1. Values greater than 50
          // 2. Even indices
          return value > 50 || dataIndex % 2 === 0;
        },
        formatter: function(value) {
          return value > 50 ? '⭐ ' + value : value;
        },
        color: '#1F2937',
        font: { weight: 'bold' }
      }
    }
  }
});
```

### Clipping to Chart Area

```javascript
const chart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    datasets: [{
      data: [10, 45, 23, 67, 89, 120],
      borderColor: '#8B5CF6'
    }]
  },
  options: {
    scales: {
      y: {
        max: 100  // Some values exceed the visible scale
      }
    },
    plugins: {
      datalabels: {
        anchor: 'end',
        align: 'end',
        offset: 4,
        clip: true,  // Clip labels extending outside chart area
        backgroundColor: 'rgba(0, 0, 0, 0.8)',
        color: 'white',
        borderRadius: 3,
        padding: 4,
        font: { size: 11 }
      }
    }
  }
});
// Labels for values > 100 will be clipped at the chart boundary
```

## TypeScript Support

### TypeScript Interface Usage

```typescript
import { Chart, ChartConfiguration } from 'chart.js';
import ChartDataLabels from 'chartjs-plugin-datalabels';
import { Context } from 'chartjs-plugin-datalabels';

Chart.register(ChartDataLabels);

const config: ChartConfiguration = {
  type: 'bar',
  data: {
    labels: ['Q1', 'Q2', 'Q3', 'Q4'],
    datasets: [{
      label: 'Revenue',
      data: [45000, 67000, 52000, 89000],
      datalabels: {
        color: '#FFFFFF',
        backgroundColor: '#000000',
        borderRadius: 4,
        padding: 6,
        font: {
          weight: 'bold',
          size: 14
        },
        formatter: (value: number, context: Context): string => {
          return '$' + (value / 1000).toFixed(0) + 'K';
        }
      }
    }]
  },
  options: {
    plugins: {
      datalabels: {
        anchor: 'end',
        align: 'top',
        display: (context: Context): boolean => {
          return context.dataset.data[context.dataIndex] as number > 50000;
        }
      }
    }
  }
};

const ctx = document.getElementById('myChart') as HTMLCanvasElement;
const chart = new Chart(ctx, config);
```

### Typed Event Listeners

```typescript
import { Chart, ChartConfiguration, ChartEvent } from 'chart.js';
import ChartDataLabels from 'chartjs-plugin-datalabels';
import { Context } from 'chartjs-plugin-datalabels';

Chart.register(ChartDataLabels);

interface CustomContext extends Context {
  selected?: boolean;
  hovered?: boolean;
}

const config: ChartConfiguration = {
  type: 'doughnut',
  data: {
    labels: ['Category A', 'Category B', 'Category C'],
    datasets: [{
      data: [300, 150, 100],
      backgroundColor: ['#FF6384', '#36A2EB', '#FFCE56']
    }]
  },
  options: {
    plugins: {
      datalabels: {
        color: 'white',
        font: {
          weight: 'bold',
          size: 16
        },
        listeners: {
          click: (context: CustomContext, event: ChartEvent): boolean => {
            context.selected = !context.selected;
            console.log('Selected:', context.selected);
            console.log('Data index:', context.dataIndex);
            console.log('Dataset index:', context.datasetIndex);
            return true;  // Update chart
          },
          enter: (context: CustomContext, event: ChartEvent): boolean => {
            context.hovered = true;
            return true;
          },
          leave: (context: CustomContext, event: ChartEvent): boolean => {
            context.hovered = false;
            return true;
          }
        },
        backgroundColor: (context: CustomContext): string => {
          if (context.selected) return 'rgba(0, 255, 0, 0.8)';
          if (context.hovered) return 'rgba(0, 0, 0, 0.9)';
          return 'rgba(0, 0, 0, 0.7)';
        }
      }
    }
  }
};

const ctx = document.getElementById('myChart') as HTMLCanvasElement;
const chart = new Chart(ctx, config);
```

## Summary

chartjs-plugin-datalabels provides comprehensive label display capabilities for Chart.js visualizations across all chart types including bar, line, pie, doughnut, radar, polar area, bubble, and scatter charts. The plugin excels at transforming raw data into readable annotations through its flexible formatter function, which supports custom logic, built-in JavaScript functions, and access to contextual information like data indices and dataset properties. It seamlessly integrates into Chart.js workflows with three configuration levels—global defaults, chart-specific options, and dataset overrides—enabling precise control over label appearance and behavior.

The plugin's positioning system combines anchor points, alignment presets, rotation, and offset values to place labels exactly where needed, whether inside elements, at boundaries, or floating nearby. Advanced features include multiple independent labels per data point using the `labels` object, scriptable options that dynamically compute styles based on data values and chart state, event listeners for click and hover interactions, automatic overlap detection with `display: 'auto'`, and clipping support for constrained layouts. With full TypeScript support and extensive styling options covering colors, fonts, backgrounds, borders, shadows, and opacity, chartjs-plugin-datalabels delivers professional-grade data labeling for both simple value displays and complex interactive visualizations.
